from itertools import product
from math import ceil
import numpy as np
import rasterio as rio
from rasterio import windows
from pathlib import Path
from functools import partial

def overlapping_windows(
    src, 
    win_height, 
    win_width, 
    h_overlap=0, 
    w_overlap=0, 
    boundless=False, 
    anchor=None
):
    
    assert isinstance(
        src, rio.io.DatasetReader
    ), "Invalid <src>! Expected it to be of type `rasterio.io.DatasetReader`"
    
    assert isinstance(
        win_width, int
    ), "Invalid <width>, Expected it to be an `int`"
    
    assert isinstance(
        win_height, int
    ), "Invalid <height>, Expected it to be an `int`"
    
    assert isinstance(
        h_overlap, int
    ), "Invalid <h_overlap>, Expected it to be an `int`"
    
    assert isinstance(
        w_overlap, int
    ), "Invalid <w_overlap>, Expected it to be an `int`"
        
    assert isinstance(
        boundless, bool
    ), "Invalid <boundless>, Expected it to be of type `bool`"
    
    hz = src.meta['height']
    wz = src.meta['width']
    hz_ = hz - 1
    wz_ = wz - 1
    dh = win_height - (2 * h_overlap)
    dw = win_width - (2 * w_overlap)
    kh = ceil(hz_ / dh)
    kw = ceil(wz_ / dw)
    h0, w0 = 0, 0
    h0_cal = hz_ - (dh * kh)
    w0_cal = wz_ - (dw * kw)
    h0_off = h0 - h_overlap
    w0_off = w0 - w_overlap
    hz_off = hz - h_overlap
    wz_off = wz - w_overlap
    h0_eq = h0_cal  // 2
    w0_eq = w0_cal  // 2
    hz_eq = hz + h0_cal - h0_eq
    wz_eq = wz + w0_cal - w0_eq
    
    if anchor is None:
        h_start = h0_off
        w_start = w0_off
        h_end = hz_off
        w_end = wz_off
    elif anchor == 'topleft':
        h_start = h0
        w_start = w0
        h_end = hz
        w_end = wz
    elif anchor == 'bottomleft':
        h_start = h0_cal
        w_start = w0
        h_end = hz
        w_end = wz_off
    elif anchor == 'bottomright':
        h_start =  h0_cal
        w_start =  w0_cal
        h_end = hz
        w_end = wz
    elif anchor == 'topright':
        h_start = h0
        w_start = w0_cal
        h_end = hz
        w_end = wz
    elif anchor == 'top':
        h_start = h0
        w_start = w0_off
        h_end = hz
        w_end = wz_off
    elif anchor == 'left':
        h_start = h0_off
        w_start = w0
        h_end = hz_off
        w_end = wz
    elif anchor == 'bottom':
        h_start = h0_cal
        w_start = w0_off
        h_end = hz
        w_end = wz_off
    elif anchor == 'right':
        h_start = h0_off
        w_start = w0_cal
        h_end = hz_off
        w_end = wz
    elif anchor == 'top-qual':
        h_start = h0
        w_start = w0_eq
        h_end = hz
        w_end = wz_eq
    elif anchor == 'left-equal':
        h_start = h0_eq
        w_start = w0
        h_end = hz_eq
        w_end = wz
    elif anchor == 'bottom-equal':
        h_start = h0_cal
        w_start = w0_eq
        h_end = hz
        w_end = wz_eq
    elif anchor == 'right-equal':
        h_start = h0_eq
        w_start = w0_cal
        h_end = hz_eq
        w_end = wz
    elif anchor == 'all-equal':
        h_start = h0_eq
        w_start = w0_eq
        h_end = hz_eq
        w_end = wz_eq
    else:
        raise AssertionError("Invalid value for parameter <anchor>!")
    
    w_offsets = range(w_start, w_end, dw)
    h_offsets = range(h_start, h_end, dh)
    
    offsets = product(
        w_offsets, 
        h_offsets
    )
    
    indices = product(
        range(0, len(w_offsets), 1),
        range(0, len(h_offsets), 1)
    )
    
    for index, (col_off, row_off) in zip(indices, offsets):
        window = windows.Window(
            col_off=col_off,
            row_off=row_off,
            width=win_width,
            height=win_height
        )

        if boundless:
            yield index, window
        else:
            yield index, window.intersection(big_window)
            

def get_tiles(
    img_path,
    win_height,
    win_width,
    h_overlap=0,
    w_overlap=0,
    boundless=True,
    anchor='topleft',
):
    if isinstance(img_path, str):
        img_path = Path(img_path)
    assert isinstance(img_path, Path), "Invalid type for parameter <img_path>! Expected `str` or `pathlib.Path`"
    assert img_path.is_file(), "Image file does not exist or not accessible!"
    
    with rio.open(img_path, 'r') as im_fp:
        if base_name is None:
            base_name = img_path.stem
        else:
            assert isinstance(base_name, str)
        ext = img_path.suffix
        for index, window in overlapping_windows(
            src=im_fp, 
            win_height=win_height, 
            win_width=win_width, 
            h_overlap=h_overlap, 
            w_overlap=w_overlap, 
            boundless=boundless, 
            anchor=anchor
        ):
            im_arr = im_fp.read(window=window, boundless=boundless, masked=True)
            yield (index[1], index[0]), im_arr