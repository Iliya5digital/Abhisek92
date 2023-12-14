labeled_data = None
fgroups = aoi_df.groupby(['FileName'])
for f in u_files:
    g = fgroups.get_group(f)
    plist, clist = g['Polygon'].tolist(), g['ClassName'].tolist()
    fpath = img_dir / f
    class_im = None
    with rio.open(fpath) as imptr:
        class_im = np.zeros(shape=imptr.shape, dtype=int)
        for ply, lbl in zip(plist, clist):
            class_im += create_image_mask(a_polygon=ply, class_name=lbl, img_shape=imptr.shape)
        if class_im.max() <= max(label_map.values()):
            data_stack = np.concatenate((img_arr, class_im.reshape(-1, *class_im.shape)), axis=0)
            flat_mask = class_im == 0
            im_mask = np.repeat(flat_mask.reshape(-1, *flat_mask.shape), data_stack.shape[0], axis=0)
            masked_data = np.ma.masked_array(data_stack, im_mask, fill_value=0, dtype=int)
            mshp = masked_data.shape
            flattened_data = np.moveaxis(masked_data, 0, -1).reshape(-1, *mshp[:1])
            flattened_data = flattened_data.filled()
            # Filter if class==0. Can be commented if unnecessary
            flattened_data = flattened_data[flattened_data[:, -1] != 0]
            if labeled_data is None:
                labeled_data = flattened_data
            else:
                labeled_data = np.concatenate((labeled_data, flattened_data), axis=0)
        else:
            print('Error in file: ' + fpath.name + fpath.suffix)

#Save Prepared data to file
labeled_data.dump('foo.npy')