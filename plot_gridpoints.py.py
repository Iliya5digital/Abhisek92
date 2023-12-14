import warnings
import numpy as np
import rasterio as rio
from pathlib import Path
from matplotlib import pyplot as plt

def grid_smapling(src_path, n, band=1):
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore", category=rio.errors.NotGeoreferencedWarning
        )
        with rio.open(src_path, 'r') as src:
            h = src.height
            w = src.width
            nh = np.around((((n * h) / w) ** 0.5), decimals=0).astype(int)
            nw = np.around((((n * w) / h) ** 0.5), decimals=0).astype(int)
            h_gap = h / nh
            w_gap = w / nw
            h_marks = h_gap * np.arange(start=0, stop=nh, step=1)
            w_marks = w_gap * np.arange(start=0, stop=nw, step=1)
            h_marks = np.around((h_marks + (h_gap / 2)), decimals=0).astype(int)
            w_marks = np.around((w_marks + (w_gap / 2)), decimals=0).astype(int)
            h_marks, w_marks = np.meshgrid(h_marks, w_marks)
            h_marks = h_marks.ravel()
            w_marks = w_marks.ravel()
            arr = src.read(band)
            z = arr[h_marks, w_marks]
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.imshow(arr)
            ax.scatter(w_marks, h_marks, c='r')
            plt.show()
    x, y = rio.transform.xy(src.transform, h_marks, w_marks)
    return x, y, z

if __name__ == '__main__':
    _ = grid_smapling('test_vario.tif', 1000, 1)
