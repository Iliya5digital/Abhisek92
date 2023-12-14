import numpy as np
import rasterio as rio

def set_nodata(image_path, nodata=0):
    with rio.open(image_path, 'r+') as src:
        src.nodata = np.array(nodata, dtype=np.dtype(src.meta['dtype'])).item()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description=(
            'Set user provided no-data value to specified geo-image'
        )
    )
    parser.add_argument(
        '-i', '--input',
        metavar='Input Image',
        action='store',
        type=str,
        required=True,
        dest='import_path',
        help='Specify input image path'
    )
    parser.add_argument(
        '-v', '--value',
        metavar='No-data Value',
        action='store',
        type=str,
        required=True,
        dest='nd',
        help='Specify no-data value'
    )
    args = parser.parse_args()
    set_nodata(args.import_path, float(args.nd))
