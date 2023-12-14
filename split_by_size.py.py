import rasterio as rio
from pathlib import Path
from rasterio.windows import Window

src_path = Path("")
dst_dir = Path("")
tile_lengths = (1, 1)

with rio.open(src_path, 'r') as src:
    meta = src.meta.copy()
    tile_height, tile_width = (np.array(tile_lengths) / np.array(src.res)).tolist()
    total_window = Window(0, 0, src.height, src.width)
    x0, y0 = np.meshgrid(
        np.arange(0, src.height, tile_height),
        np.arange(0, src.width, tile_width)
    )
    x0, y0 = x0.ravel().tolist(), y0.ravel().tolist()
    for xa, ya in zip(x0, y0):
        dst_path = dst_dir / f"{src_path.stem}_{xa}_{ya}{src_path.suffix}"
        w = Window(xa, ya, tile_height, tile_width).intersection(total_window)
        arr = src.read(window=w)
        meta['count'], meta['height'], meta['width'] = arr.shape
        meta['transform'] = src.window_transform(w)
        with rio.open(dst_path, 'w', **meta) as dst:
            dst.write(arr)