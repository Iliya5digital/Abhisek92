import os
import gdal
import numpy as np
import rasterio as rio
from pathlib import Path
from random import shuffle
from math import floor, ceil
from itertools import product
from rasterio import windows as rio_windows

def generate_windows(
    img_height, 
    img_width, 
    win_height, 
    win_width, 
    min_hoverlap, 
    min_woverlap, 
    boundless=False
):
    hc = ceil((img_height - min_hoverlap) / (win_height - min_hoverlap))
    wc = ceil((img_width - min_woverlap) / (win_width - min_woverlap))
    
    
    h_overlap = ((hc * win_height) - img_height) // (hc - 1)
    w_overlap = ((wc * win_height) - img_width) // (wc - 1)
    
    
    hslack_res = ((hc * win_height) - img_height) % (hc - 1)
    wslack_res = ((wc * win_width) - img_width) % (wc - 1)
    
    dh = win_height - h_overlap
    dw = win_width - w_overlap
    
    row_offsets = np.arange(0, (img_height-h_overlap), dh)
    col_offsets = np.arange(0, (img_width-w_overlap), dw)
    
    if hslack_res > 0:
        row_offsets[-hslack_res:] -= np.arange(1, (hslack_res + 1), 1)
    if wslack_res > 0:
        col_offsets[-wslack_res:] -= np.arange(1, (wslack_res + 1), 1)
    
    row_offsets = row_offsets.tolist()
    col_offsets = col_offsets.tolist()
    
    offsets = product(col_offsets, row_offsets)
    
    indices = product(range(len(col_offsets)), range(len(row_offsets)))
    
    big_window = rio_windows.Window(col_off=0, row_off=0, width=img_width, height=img_height)
    
    for index, (col_off, row_off) in zip(indices, offsets):
        window = rio_windows.Window(
            col_off=col_off,
            row_off=row_off,
            width=win_width,
            height=win_height
        )
        if boundless:
            yield index, window
        else:
            yield index, window.intersection(big_window)

def generate_image_tiles(
    img_path,
    win_height, 
    win_width, 
    min_hoverlap, 
    min_woverlap, 
    dst_dir,
    boundless=False,
    dst_driver='GTiff',
    dst_ext='tif',
    dst_base=None,
):
    tile_list = list()
    with rio.open(img_path, 'r') as src:
        meta = src.meta.copy()
        img_height = src.height
        img_width = src.width
        for idx, w in generate_windows(
            img_height=img_height, 
            img_width=img_width, 
            win_height=win_height, 
            win_width=win_width, 
            min_hoverlap=min_hoverlap, 
            min_woverlap=min_woverlap, 
            boundless=False
        ):
            w_arr = src.read(window=w, masked=True)
            if not(np.all(w_arr.mask)):
                w_transform = rio_windows.transform(
                    window=w, 
                    transform=src.transform
                )
                meta['count'], meta['height'], meta['width'] = w_arr.shape
                meta['transform'] = w_transform
                meta['driver'] = dst_driver
                if dst_base is None:
                    dst_base = img_path.stem
                d_dir = Path(dst_dir / 'Tiles')
                d_dir.mkdir(parents=True, exist_ok=True)
                dst_path = d_dir / '{}_{}_{}.{}'.format(
                    dst_base, idx[0], idx[1], dst_ext
                )
                with rio.open(dst_path, 'w', **meta) as dst:
                    dst.write(w_arr)
                tile_list.append(dst_path.relative_to(Path(dst_dir)))
    return tile_list


def split_tiles(tile_list, ratio=(8, 1, 1)):
    denominator = sum(ratio)
    sorted_index = sorted(
        range(len(ratio)), 
        key=lambda k: ratio[k],
        reverse=True
    )
    
    part_sizes = list()
    remaining = len(tile_list)
    for  i in sorted_index:
        c = ceil((ratio[i] * len(tile_list)) / denominator)
        if c > remaining:
            c = remaining
        remaining -= c
        part_sizes.append(c)

    part_sizes = [
        x for _, x in sorted(
            zip(sorted_index, part_sizes), key=lambda pair: pair[0]
        )
    ]
    assert not(0 in part_sizes), 'Unslovable with given ratio!!'
    shuffle(tile_list)
    parts = list()
    start = 0
    for delta in part_sizes:
        end = start + delta
        parts.append(tile_list[start:end])
        start = end
    return parts

def build_vrt(tile_list, dst_path, **vrt_options):
    v_ops = gdal.BuildVRTOptions(**vrt_options)
    gdal.BuildVRT(
        destName=str(dst_path), 
        srcDSOrSrcDSTab=[str(t) for t in tile_list], 
        options=v_ops
    )
    

if __name__ == '__main__':
    img_path = Path('Potsdam_2_10_RGBIR.tif')
    win_height = 600
    win_width = 600
    min_hoverlap = 0
    min_woverlap = 0
    dst_dir = Path('Test')
    im_tiles = generate_image_tiles(
        img_path=img_path,
        win_height=win_height,
        win_width=win_width,
        min_hoverlap=min_hoverlap,
        min_woverlap=min_woverlap,
        dst_dir=dst_dir
    )
    
    wd = Path(os.getcwd())
    os.chdir(dst_dir)
    
    s_parts = split_tiles(im_tiles)
    dpaths = (
        Path('Test/Train.vrt'),
        Path('Test/Validation.vrt'),
        Path('Test/Test.vrt')
    )
    for p, dp in zip(s_parts, dpaths):
        build_vrt(
            tile_list=p, 
            dst_path=dp.relative_to(dst_dir), 
            resampleAlg='near', 
            addAlpha=False
        )
    os.chdir(wd)
