import numpy as np
from numpy.lib.stride_tricks import as_strided


def convoly(array_in, kernel):
    if len(array_in.shape) == len(kernel.shape):
        parent_shape = tuple((np.array(array_in.shape) - (np.array(kernel.shape) - 1)).tolist())
        shaper = parent_shape + kernel.shape
        strider = 2 * array_in.strides
        expanded_input = as_strided(
            array_in,
            shape=shaper,
            strides=strider,
            writeable=False,
        )
        return expanded_input

def image_filter(img_array, kernel):
    expanded_input = convoly(img_array, kernel)
    filtered_img = np.einsum(
        'xyij,ij->xy',
        expanded_input,
        kernel,
    )
    return filtered_img

def convol_flat(array_in, kernel):
    expanded_array = convoly(array_in, kernel)
    out_shape = list(expanded_array.shape[:-1])
    out_shape[-1] = expanded_array.shape[-1] * expanded_array.shape[-2]
    out_shape = tuple(out_shape)
    #print(out_shape)
    out_array = expanded_array.reshape(out_shape)
    return out_array