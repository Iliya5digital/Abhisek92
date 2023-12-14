import numpy as np

def get_window(index, arr, widths):
    if len(index) == len(arr.shape) == len(widths):
        index = np.array(index)
        max_indices = np.array(arr.shape)
        widths = np.array(widths)
        win_start = index - widths
        win_end = index + (widths + 1)     
        win_start[win_start < 0] = 0
        max_mask = win_end > max_indices
        win_end = (max_mask * max_indices) + (~max_mask * win_end)
        indexer = tuple(map(slice, win_start, win_end))
        return  arr[indexer]
    else:
        raise ValueError("Shape mismatch!")

def generate_indices(arr_shape):
    idx = np.indices(arr_shape)
    dt = ('int, ' * idx.shape[0])[:-2]
    i = 0
    out = np.zeros(arr_shape, dtype=dt)
    for indx in list(out.dtype.fields.keys()):
        out[indx] = idx[i]
        i += 1
    return out.astype(object)


vget_window = np.vectorize(get_window, excluded=['arr', 'widths'], otypes=[object])


def convolve_function(arr, widths, vfunc):
    indxs = generate_indices(arr.shape)
    slices = vget_window(index=indxs, arr=arr, widths=widths)
    return vfunc(slices)