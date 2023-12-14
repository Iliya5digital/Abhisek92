#!/usr/bin/env python


import gdal
import numpy
import os


def __main():
    abspath = os.path.abspath(__file__)
    dir_name = os.path.dirname(abspath)
    os.chdir(dir_name)

    #Change The Filenames Accordingly
    original = gdal.Open(r'aoi.img')
    brovey = gdal.Open(r'brovey.img')
    ehlers = gdal.Open(r'ehlers.img')
    hpf = gdal.Open(r'hpf.img')
    multi = gdal.Open(r'multiplicative.img')
    pca = gdal.Open(r'pca.img')
    wavelet = gdal.Open(r'wavelet.img')
    
    print(get_rmse(original, multi))
    print(get_quality(original, brovey))
    print(get_correlation(original, brovey))
    print(get_relative_mean(original, brovey))
    print(get_entropy(brovey))
    print(get_std_dev(original))


def get_rmse(orig, ref):
    try:
        if orig.RasterCount == ref.RasterCount:
            count = orig.RasterCount
            rmse_vector = list()
            for i in range(count):
                current_band = (numpy.array(orig.GetRasterBand(i+1).ReadAsArray())).astype(float)
                ref_band = (numpy.array(ref.GetRasterBand(i+1).ReadAsArray())).astype(float)
                rmse_vector.append(numpy.sqrt(((numpy.subtract(current_band, ref_band)) ** 2).mean()))
            return rmse_vector
        else:
            raise IOError("No of Bands does not match")
    except IOError as dim_error:
        print(dim_error)
        return None


def covarience(orig, ref):
    try:
        if orig.shape == ref.shape:
            return ((numpy.sum(numpy.multiply((orig - orig.mean()), (ref - ref.mean())))).prod()) / (ref.size - 1)
        else:
            raise IOError("Dimension Mismatch")
    except IOError as dim_error:
        print(dim_error)
        return None


def quality(orig, ref):
    try:
        if orig.shape == ref.shape:
            numerator = 4 * covarience(orig, ref) * (orig.mean() * ref.mean())
            denominator = ((orig.mean()**2) + ((ref.mean()**2))) * ((numpy.var(orig.ravel())) + (numpy.var(ref.ravel())))
            return numerator / denominator
        else:
            raise IOError("Dimension Mismatch")
    except IOError as dim_error:
        print(dim_error)
        return None


def get_covariance(orig, ref):
    try:
        if orig.RasterCount == ref.RasterCount:
            count = orig.RasterCount
            cov_vector = list()
            for i in range(count):
                current_band = (numpy.array(orig.GetRasterBand(i+1).ReadAsArray())).astype(float)
                ref_band = (numpy.array(ref.GetRasterBand(i+1).ReadAsArray())).astype(float)
                cov_vector.append(covarience(current_band, ref_band))
            return cov_vector
        else:
            raise IOError("No of Bands does not match")
    except IOError as dim_error:
        print(dim_error)
        return None


def get_quality(orig, ref):
    try:
        if orig.RasterCount == ref.RasterCount:
            count = orig.RasterCount
            quality_vector = list()
            for i in range(count):
                current_band = (numpy.array(orig.GetRasterBand(i+1).ReadAsArray())).astype(float)
                ref_band = (numpy.array(ref.GetRasterBand(i+1).ReadAsArray())).astype(float)
                quality_vector.append(quality(current_band, ref_band))
            return quality_vector
            
        else:
            raise IOError("No of Bands does not match")
    except IOError as dim_error:
        print(dim_error)
        return None

     
def correlation(orig, ref):
    try:
        if orig.shape == ref.shape:
                        numerator = (2 * numpy.sum(numpy.multiply(orig, ref)))
                        denominator = (numpy.sum((orig**2)) + numpy.sum((ref**2)))
                        return numerator / denominator
        else:
            raise IOError("Dimension Mismatch")
    except IOError as dim_error:
        print(dim_error)
        return None


def get_correlation(orig, ref):
    try:
        if orig.RasterCount == ref.RasterCount:
            count = orig.RasterCount
            correlation_vector = list()
            for i in range(count):
                current_band = (numpy.array(orig.GetRasterBand(i+1).ReadAsArray())).astype(float)
                ref_band = (numpy.array(ref.GetRasterBand(i+1).ReadAsArray())).astype(float)
                correlation_vector.append(correlation(current_band, ref_band))
            return correlation_vector
            
        else:
            raise IOError("No of Bands does not match")
    except IOError as dim_error:
        print(dim_error)
        return None


def relative_mean(orig, ref):
    try:
        if orig.shape == ref.shape:
            return ((ref.mean() - orig.mean()) * 100) / ref.mean()
        else:
            raise IOError("Dimension Mismatch")
    except IOError as dim_error:
        print(dim_error)
        return None


def get_relative_mean(orig, ref):
    try:
        if orig.RasterCount == ref.RasterCount:
            count = orig.RasterCount
            relative_vector = list()
            for i in range(count):
                current_band = (numpy.array(orig.GetRasterBand(i+1).ReadAsArray())).astype(float)
                ref_band = (numpy.array(ref.GetRasterBand(i+1).ReadAsArray())).astype(float)
                relative_vector.append(relative_mean(current_band, ref_band))
            return relative_vector
            
        else:
            raise IOError("No of Bands does not match")
    except IOError as dim_error:
        print(dim_error)
        return None


def entropy(img):
    try:
        size_dict = {1:8, 2:16, 3:32}
        if img.DataType in (1, 2, 4):
            img_matrix = (numpy.array(img.ReadAsArray())).astype(float)
            upper = (2 ** size_dict[img.DataType]) - 1
            p_dist = numpy.histogram(img_matrix, bins=upper, range=(0, upper), density=True)[0]
            return -1 * numpy.sum(numpy.multiply(p_dist, numpy.log2(p_dist, out=numpy.zeros_like(p_dist, dtype=numpy.float), where=p_dist > 0)))
        else:
            raise TypeError("Only Unsigned Integer Datatypes are Supported")
    except TypeError as type_error:
        print(type_error)
        return None


def get_entropy(orig):  
    count = orig.RasterCount
    entropy_vector = list()
    for i in range(count):
        current_band = orig.GetRasterBand(i+1)
        entropy_vector.append(entropy(current_band))
    return entropy_vector


def get_std_dev(img):
    count = img.RasterCount
    sd_vector = list()
    for i in range(count):
        current_band = (numpy.array(img.GetRasterBand(i+1).ReadAsArray())).astype(float)
        sd_vector.append(numpy.std(current_band))
    return sd_vector

if __name__ == '__main__':
    __main()