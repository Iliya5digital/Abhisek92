import rasterio as rio
from pathlib import Path
import rasterio.mask as rio_mask
from shapely.geometry import box
from rasterio.vrt import WarpedVRT

img_path = Path("")
dem_path = Path("")
dst_path = Path("")

with rio.open(src_path, 'r') as img, rio.open(dem_path, 'r') as dem:
    with WarpedVRT(dem, crs=img.crs) as dem_vrt:
        meta = dem_vrt.meta.copy()
        bbox = box(*img.bounds)
        dst_img, dst_transform = rio_mask.mask(
          dataset=dem_vrt,
          shapes=(bbox,),
          invert=False,
          all_touched=False,
          crop=True,
          filled=True
        )
        meta['driver'] = 'GTiff'
        meta['count'], meta['height'], meta['width'] = dst_img.shape
        meta['transform'] = dst_transform
        with rio.open(dst_path, 'w', **meta) as dst:
            dst.write(dst_img)
