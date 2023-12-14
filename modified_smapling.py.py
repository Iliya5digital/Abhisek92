def grid_smapling(src_path, n=None, band=1):
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore", category=rio.errors.NotGeoreferencedWarning
        )
        with rio.open(src_path, 'r') as src:
            arr = src.read(band)
            if isinstance(n, int) and n > 0:
                h = src.height
                w = src.width
                nh = np.around((((n * h) / w) ** 0.5), decimals=0).astype(int)
                nw = np.around((((n * w) / h) ** 0.5), decimals=0).astype(int)
                h_gap = h / (nh + 2)
                w_gap = w / (nw + 2)
                h_marks = np.around(
                    (h_gap * np.arange(start=1, stop=(nh+2), step=1)), decimals=0
                ).astype(int)
                w_marks = np.around(
                    (w_gap * np.arange(start=1, stop=(nw+2), step=1)), decimals=0
                ).astype(int)
                h_marks, w_marks = np.meshgrid(h_marks, w_marks)
                h_marks = h_marks.ravel()
                w_marks = w_marks.ravel()
                z = arr[h_marks, w_marks]
            else:
                h_len, w_len = arr.shape
                z = arr.ravel()
                h_marks, w_marks = np.meshgrid(
                    np.arange(h_len), np.arange(w_len)
                )
                h_marks = h_marks.ravel()
                w_marks = w_marks.ravel()
    x, y = rio.transform.xy(src.transform, h_marks, w_marks)
    return x, y, z
