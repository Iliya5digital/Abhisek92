def extract_pixels(imgfile, shapefile, attributes=None, all_touched=True):
    lbl_flag = False
    with fiona.open(shapefile) as shp_fp:
        with rio.open(imgfile, 'r') as img_fp:
            feature_vectors, label_vectors = list(), list()
            for feature in shp_fp:
                if feature["geometry"]['type'] in ("MultiPolygon", "Polygon"):
                    masked_box, _ = rio_mask(
                        dataset=img_fp, 
                        shapes=[feature["geometry"],], 
                        all_touched=all_touched, 
                        crop=True, 
                        filled=False, 
                        pad=False
                    )
                    # RasterIO Reads Bands First
                    bandwise_pixeldump = list()
                    for i in range(masked_box.shape[0]):
                        assert (
                            masked_box[0].mask == masked_box[i].mask
                        ).all(), "Band-wise Mask Mismatch! <Band {}>".format(i)
                        bandwise_pixeldump.append(masked_box[i].compressed())
                    pixel_dump = np.stack(bandwise_pixeldump, axis=-1)
                    if attributes and isinstance(attributes, (str, tuple, list)):
                        if isinstance(attributes, str):
                            attributes = (attributes,)
                        bandwise_labeldump = list()
                        for attr in attributes:
                            assert attr in shp_fp.schema[
                                'properties'
                            ].keys(), "Provided Attribute({}) not found in data!".format(
                                attr
                            )
                            lbl_flag = True
                            fill_val = feature['properties'][attr]
                            if np.issubdtype(type(fill_val), np.number):
                                proxy_array = np.full_like(
                                    bandwise_pixeldump[-1], 
                                    fill_val
                                )
                            else:
                                proxy_array = np.full_like(
                                    bandwise_pixeldump[-1], 
                                    fill_val, 
                                    dtype=object
                                )
                            bandwise_labeldump.append(proxy_array)
                        label_dump = np.stack(bandwise_labeldump, axis=-1)
                        label_vectors.append(label_dump)
                    feature_vectors.append(pixel_dump)
            if len(feature_vectors) > 0:
                feature_vectors = np.concatenate(feature_vectors, axis=0)
            else:
                feature_vectors = np.array([])
            if len(label_vectors) > 0:
                assert len(label_vectors) == len(label_vectors), "Label Vector Count and Feature Vector Count Mismatch!"
                label_vectors = np.concatenate(label_vectors, axis=0)
            else:
                label_vectors =  np.array([])
            if lbl_flag:
                return feature_vectors, label_vectors
            else:
                return feature_vectors