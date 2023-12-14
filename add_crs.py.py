from pathlib import Path
import rasterio as rio
from tqdm import tqdm

src_path = Path('multispectral_path')
tiles_dir = Path("path/Tiles")

with rio.open(src_path, 'r') as src:
    crs = src.meta['crs']
for fp in tqdm(list(tiles_dir.glob("*.tif"))):
    with rio.open(fp, 'r+') as tile:
        tile.crs = crs