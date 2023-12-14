from pathlib import Path
import rasterio as rio
import numpy as np

src_path = Path("")
dst_path = Pat("")
downscale_factor = 10.0

with rio.open(src_path, 'r') as src:
    meta = src.meta.copy()
    src_t = meta['transform']
    view_h = int(meta['height'] / downscale_factor)
    view_w = int(meta['width'] / downscale_factor)
    
    view = src.read(
        out_shape=(view_h, view_w),
        resampling=1,
        boundless=False
    )
    
    meta['height'] = view_h
    meta['width'] = view_w
    meta['transform'] = src_t * src_t.scale(downscale_factor, downscale_factor)
    with rio.open(dst_path, 'w', **meta) as dst:
        dst.write(view)
