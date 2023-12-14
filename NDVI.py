def calc_ndvi(img, r_id=3, n_id=4, out_file="NDVI.tif"):

    out = None
    with rio.open(img, 'r') as src:
        kwargs = src.profile
        red = src.read(r_id).astype(float)
        nir = src.read(n_id).astype(float)
        if kwargs['nodata'] in (np.nan, np.inf):
            red = np.ma.masked_array(red, mask=~np.isfinite(red))
            nir = np.ma.masked_array(nir, mask=~np.isfinite(nir))
        else:
            red = np.ma.masked_array(red, mask=(red == kwargs['nodata']))
            nir = np.ma.masked_array(nir, mask=(nir == kwargs['nodata']))
        nu = nir - red
        de = nir + red
        de = np.ma.masked_array(de, mask=(de == 0))
        ndvi_band = (nu / de).astype(float)
        np.ma.set_fill_value(ndvi_band, np.nan)
        kwargs.update(driver='GTiff', count=1, dtype='float32', tiled=True, nodata=np.nan)
        with rio.open(out_file, 'w+', **kwargs) as dst:
            dst.write(ndvi_band.data.astype(np.float32), 1)
        out = ndvi_band.astype(np.float32)
    return out