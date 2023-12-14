import numpy as np
from scipy.stats import binom


def calc(
    n, k, theta, l1, l2, sigma1, sigma2 length, dist='ge'
):
    
    big_k = 2 * k * np.sin(theta)
    sa = sigma1 ** 2
    sb = sigma2 ** 2
    a = sa / (sa + sb)
    b = sb / (sa + sb)
    
    def f_ge(m):
        x = binom.pmf(m, n, a)
        c = ((l2 ** 2) / (2 * m)) * np.exp(
            -(((big_k * l2) ** 2) / (4 * m))
        )
        return x * c
    
    def f_e(m):
        x = binom.pmf(m, n, a)
        lt2 = ((l1 * l2) / (((n - m) * l2) + ( m * l1))) ** 2
        c = lt2 * ((1 + ((big_k ** 2) * lt2)) ** (-1.5))
        return x * c
    
    def f_g(m):
        x = binom.pmf(m, n, a)
        le2 = ((l1 * l2) ** 2) / (((n - m) * (l2 ** 2)) + ( m * (l1 ** 2)))
        c = (le2 / 2) * np.exp(((big_k ** 2) * le2) / -4)
        return x * c
    
    fge = np.vectorize(f_ge)
    fe = np.vectorize(f_e)
    fg = np.vectorize(f_g)
    
    if dist.lower() == 'ge':
        t1 = (
            (a ** n ) * ((l1 / n) ** 2) * (
                (1 + (((big_k * l1) / n) ** 2)) ** 1.5
            )
        ) + (
            (b ** n ) * ((l2 ** 2) / (2 * n)) * np.exp(
                -(((big_k * l2) ** 2) / (4 * n))
            )
        )
        t2 = np.sum(fge(np.arange(1, n)))
        return t1 + t2
    elif dist.lower() == 'e':
        return np.sum(fe(np.arange((n + 1))))
    elif dist.lower() == 'g':
        return np.sum(fg(np.arange((n + 1))))
    else:
        raise NotImplementedError("Unknown 'dist': {}".format(dist))
