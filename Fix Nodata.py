import numpy as np
import rasterio as rio
from rasterio.features import sieve

def generate_mask(imgfile, out_img=None, current_nd=0, target_nd=-99999, size=500):
    with rio.open(imgfile, 'r') as src:
        meta = src.meta.copy()
        img_array = src.read(masked=False)
        mask = img_array == current_nd
        mask =  mask.any(axis=0)
        #mask = np.stack((mask for i in range(img_array.shape[0])), axis=0)
        mask =  np.iinfo(np.uint8).max * ((np.logical_not(mask)).astype(np.uint8))
        mask = sieve(mask, size=size)
        mask = np.logical_not(mask.astype(bool))
        mask = np.stack([mask for i in range(img_array.shape[0])], axis=0)
        img_array[mask] = target_nd
        meta['nodata'] = target_nd
    if out_img is None:
        out_img = imgfile
    with rio.open(out_img, 'w', **meta) as dst:
        dst.write(img_array)