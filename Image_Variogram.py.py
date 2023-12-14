import warnings
import numpy as np
import gstools as gs
import rasterio as rio
from pathlib import Path
from matplotlib import pyplot as plt
from gstools import (
    Gaussian,
    Exponential,
    Matern,
    Stable,
    Rational,
    Cubic,
    Circular,
    Spherical,
    HyperSpherical,
    SuperSpherical,
    JBessel
)

models_available = {
    'gaussian': Gaussian,
    'exponential': Exponential,
    'matern': Matern,
    'stable': Stable,
    'rational': Rational,
    'cubic': Cubic,
    'circular': Circular,
    'spherical': Spherical,
    'hyper_spherical': HyperSpherical,
    'super_spherical': SuperSpherical,
    'bessel': JBessel
}

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
    x, y = rio.transform.xy(src.transform, h_marks, w_marks)
    return x, y, z

def make_variogram(
    x, y, z, model=models_available['exponential']
):
    bin_center, gamma = gs.vario_estimate((x, y), z)
    fit_model = model(
        dim=2,
        var=1.0,
        len_scale=1.0,
        nugget=0.0,
        anis=1.0,
        angles=0.0,
        integral_scale=None,
        rescale=None,
        latlon=False,
        var_raw=None,
        hankel_kw=None
    )
    fit_model.fit_variogram(bin_center, gamma, nugget=True)
    return fit_model, bin_center, gamma

def plot_variogram(fit_model, bin_center, gamma, save_fig='/tmp/foo.png'):
    if save_fig:
        ax = fit_model.plot(x_max=max(bin_center))
        ax.scatter(bin_center, gamma)
        plt.savefig(save_fig)
        del ax

if __name__ == '__main__':
    img_path = Path("test_vario.tif")
    dst_dir = '/tmp'
    x, y, z = grid_smapling(img_path, n=10000, band=1)
    out = make_variogram(x, y, z, models_available['matern'])
    plot_variogram(*out, '/tmp/foo.png')
    #for m in models_available.keys():
        #out = make_variogram(
            #x, y, z, models_available[m], f'/tmp/Figs/{m}.png'
        #)
        #plot_variogram(*out, f'{dst_dir}/tmp/{m}.png')
