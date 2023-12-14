import argparse
import numpy as np
import rasterio as rio
from pathlib import Path
from rich.progress import track
from rasterio.windows import Window

# Comment Block- A and uncomment Block -B to run it in Notebook
# Fill the paths in Block - B accordingly 

# ================================ Block - A ================================ #
parser = argparse.ArgumentParser(
    description=("Compress GTiff Image")
)
parser.add_argument(
    '-i', '--input',
    metavar='Source Image',
    action='store',
    type=str,
    required=True,
    dest='src_path',
    help='Specify the source file path.'
)
parser.add_argument(
    '-o', '--output',
    metavar='Output Image',
    action='store',
    type=str,
    required=True,
    dest='dst_path',
    help='Specify the destination file path.'
)
args = parser.parse_args()
src_path = Path(args.src_path)
dst_path = Path(args.dst_path)
# ================================ Block - A ================================ #


# ================================ Block - B ================================ #
# src_path = Path("")
# dst_path = Path("")
# ================================ Block - B ================================ #

with rio.open(src_path, "r") as src:
    meta = src.meta.copy()

big_window = Window(row_off=0, col_off=0, height=meta["height"], width=meta["width"])
h_marks, w_marks = np.meshgrid(np.arange(0, meta["height"], 512), np.arange(0, meta["width"], 512))
h_marks, w_marks = h_marks.ravel().tolist(), w_marks.ravel().tolist()
meta["driver"] = "GTiff"
meta["TILED"] = True
meta["BLOCKXSIZE"] = 512
meta["BLOCKXYSIZE"] = 512
meta["compress"] = "zstd"
meta["SPARSE_OK"] = True
meta["NUM_THREADS"] = "ALL_CPUS"
meta["ZSTD_LEVEL"] = 22
img_dtype = np.dtype(meta["dtype"])
meta["BIGTIFF"] = True if (
    meta["height"] * meta["width"] * img_dtype.itemsize
) >= (2 ** 32) else False

if np.issubdtype(img_dtype, np.integer):
    meta["predictor"] = 2
elif np.issubdtype(img_dtype, np.inexact):
    meta["predictor"] = 3
else:
    # This should not happen
    meta["predictor"] = 1

with rio.open(src_path, "r") as src, rio.open(dst_path, "w", **meta) as dst:
    for hs, ws in track(list(zip(h_marks, w_marks)), description="Writing:"):
        win = big_window.intersection(Window(row_off=hs, col_off=ws, height=512, width=512))
        dst.write(src.read(window=win), window=win)
