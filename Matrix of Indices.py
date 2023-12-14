import numpy as np
from itertools import product

def gen_index_mat(size=2):
    if isinstance(size, int):
        if size >= 2:
            vec = list(range(size))
            lst = list(product(vec, vec))
            unpacked = np.array(lst, dtype='int, int')
            kernel = unpacked.reshape(size, size)
            return kernel


print(gen_index_mat(5))