import os
from pathlib import Path

dst_dir = Path('path')

os.chdir(dst_dir)
tiles_dir =  dst_dir / 'Tiles'

tiles = list()
for fp in tqdm(list(tiles_dir.glob("*.tif"))):
    tiles.append(str(fp.relative_to(dst_dir)))
vrt_path = dst_dir / "Mosaic_HS.VRT"
vrt_options = gdal.BuildVRTOptions(resampleAlg='near', addAlpha=False)
ds = gdal.BuildVRT(
    str(vrt_path.relative_to(dst_dir)), tiles, options=vrt_options
  )
ds.FlushCache()
