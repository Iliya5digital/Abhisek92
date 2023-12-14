import numpy as np
import rasterio as rio

def linearize(img):
    return 10.0 ** (img / 10.0)

def make_mask(img, thresold=-20.0):
    valid_mask = np.logical_not(
        (img[0, :, :] > img[1, :, :]),
        (img[0, :, :] > threshold)
    )
    return np.ma.masked_array(
        img, np.logical_not(valid_mask), fill_value=np.nan
    )


def decompose(img):
    q = img[1, :, :] / img[0, :, :]
    x = (1 - q)
    y = (1 + q)
    m_c = x / y
    theta_c = np.arctan((1 - (q ** 2)) / (x + (q ** 2)))
    p1 = 1 / y
    p2 = q * p1
    h_c = -(p1 * np.log2(p1)) + (p2 * np.log2(p2))
    return np.concatenate((m_c, theta_c, h_c), axis=0)
