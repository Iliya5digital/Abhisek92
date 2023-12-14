import numpy as np
from scipy.integrate import quad

def func(x, l, kx):
    return np.exp(
        i * (-(((x) ** 2) / l ** 2))
    ) * np.cos(2 *i * kx * x)

def sigma_vv(theta, d, h, l):
    theta = np.deg2rad(theta)
    k = (2 * np.pi) / l
    k_z = k * np.cos(theta)
    k_x = k * np.sin(theta)
    rv_n = (d * np.cos(theta))-np.sqrt(d-(np.sin(theta) ** 2))
    rv_d = (d * np.cos(theta)) + np.sqrt(d-(np.sin(theta) ** 2))
    r_v = rv_n / rv_d
    f_vv = (2 * r_v) / (np.cos(theta))
    f_vv_x = (
        2 * (np.sin(theta) ** 2
    ) * (1 + r_v) ** 2) / np.cos(theta) 
    f_vv_y = (1 - (1 / d)) + (
        (
            d - (sin(theta) ** 2) - d * (cos(theta) ** 2)
        ) / (
            (d ** 2) * (cos(theta) ** 2)
        )
    ) 
    f_vv_xy = f_vv_x * f_vv_y
    # Assuming precision of float32
    eps = np.finfo(np.float32).tiny
    assert (
        np.abs(
            np.array(
                [
                    k, 
                    k_z, 
                    k_x, 
                    r_v, 
                    f_vv, 
                    f_vv_xy
                ], 
                dtype=np.float64
            )
        ) > eps
    ).all()
    
    sigma_vv_g, i = 0.0, 0
    while True:
        i+=1
        fact_inv = np.float64(1.0 / np.float64(np.math.factorial(i)))
        if fact_inv < eps: 
            break
        else:
            # do the further calculation here
            intensity_vv = (
                (
                    (2 * k_z) ** i
                ) * f_vv * exp(
                    (-h ** 2) * (k_z ** 2)
                )
            ) + (
                ((k_z ** i) * f_vv_xy) / 2
            )
            w, err = quad(func=func, a=-np.inf, np.inf, args=(l, k_x))
            delta_i = (
                (k ** 2) / 2 
            ) * np.exp(
                (-2) * (k_z ** 2) * (h ** 2)
            ) * (
                (
                    (
                        h ** (2 * i)
                    ) * (
                        (I_vv) ** 2
                    ) * (
                        (1 / (2 * np.pi)) * w
                    )
                ) * fact_inv
            )
            if np.abs(delta_i) < eps:
                # There is no point of proceeding further since we reached the limit of precision
                break
            else:
                sigma_vv_g += delta_i