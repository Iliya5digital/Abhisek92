import numpy as np
import rasterio as rio
from rasterio.crs import CRS
from rasterio.warp import transform
from rasterio.windows import Window
from rasterio.transform import rowcol

radius = 200

gcs_moon_2000 = CRS.from_wkt(
    """GEOGCS["GCS_Moon_2000",DATUM["D_Moon_2000",SPHEROID["Moon_2000_IAU_IAG",1737400,0,AUTHORITY["ESRI","107903"]],AUTHORITY["ESRI","106903"]],PRIMEM["Reference_Meridian",0,AUTHORITY["ESRI","108900"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["ESRI","104903"]]"""
)
with rio.open("Apollo_14.tiff", "r") as src:
    res_x, res_y = src.res
    meta = src.meta.copy()
    origin_x, origin_y = transform(src_crs=gcs_moon_2000, dst_crs=meta["crs"], xs=[-17.47139], ys=[-3.64544], zs=None)
    origin_r, origin_c = rowcol(transform=meta["transform"], xs=origin_x[0], ys=origin_y[0], op=lambda x: x, precision=None)
    rx, ry = radius / res_x, radius / res_y
    row_off, col_off = round(origin_r - rx), round(origin_c - ry)
    wh, ww = round(2 * rx), round(2 * ry)
    window = Window(row_off=row_off, col_off=col_off, height=wh, width=ww)
    r, c = np.meshgrid(np.arange(0, wh), np.arange(0, ww))
    mask = (((r - (wh / 2) + 0.5) / rx) **2) + (((c - (ww / 2) + 0.5) / ry) ** 2) >= 1
    arr = src.read(window=window, masked=True, boundless=True, fill_value=meta["nodata"])
    arr.mask = np.logical_or(arr.mask, mask)
    print(arr.mean(axis=(1, 2)))