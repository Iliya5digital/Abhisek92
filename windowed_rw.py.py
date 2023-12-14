import rasterio as rio

src_path = "specify input image path"
dst_path = "specify output image path"
win_height = 1024  # Change as required
win_width = 1024  # Change as required


with rio.open(src_path, 'r') as src:
    meta = src.profile.copy()
    img_h = src.height
    img_w = src.width
    r_offsets = range(0, src.height, win_height))
    c_offsets = range(0, src.width, win_width))
    for r_off, c_off in zip(r_offsets, c_offsets):
        win = Window(row_off=r_off, col_off=c_off, height=win_height, width=win_width)
        img = src.read(window=win)
        # Do your processing here
        
        # update meta for output image as required
        # for example meta['count'] = 64 to change the no. of bands in the output image
        with rio.open(dst_path, 'w', **meta) as dst:
            dst.write(img) # Write array to file, not necessarily have to image
