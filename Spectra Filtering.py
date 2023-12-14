import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d

from matplotlib import rc
rc('text', usetex=True, aa=True)
plt.rcParams.update({'font.size': 20})
k_size = 3

df = pd.read_csv('Sample_Spectra.csv', header=0)
s1 = df[["Wavelength", "S1"]].to_numpy()
s2 = df[["Wavelength", "S2"]].to_numpy()
s3 = df[["Wavelength", "S3"]].to_numpy()
x1 = s1[:, 0]
x2 = s2[:, 0]
x3 = s3[:, 0]
y1 = s1[:, 1]
y2 = s2[:, 1]
y3 = s3[:, 1]

y1_flt = y1.copy()
x1_flt = x1.copy()
for i in range(10):
    yy1 = np.convolve(y1_flt, np.ones((k_size,))/k_size, mode='valid')
    xx1 = np.convolve(x1_flt, np.ones((k_size,))/k_size, mode='valid')
    # xx1 = x1[:yy1.size]

    # yy2 = np.convolve(y2, np.ones((k_size,))/k_size, mode='valid')
    # xx2 = np.convolve(x2, np.ones((k_size,))/k_size, mode='valid')
    # xx2 = x2[:yy2.size]

    # yy3 = np.convolve(y3, np.ones((k_size,))/k_size, mode='valid')
    # xx3 = np.convolve(x3, np.ones((k_size,))/k_size, mode='valid')
    # xx3 = x3[:yy3.size]

    f1 = interp1d(x=xx1, y=yy1, kind='linear', fill_value="extrapolate", assume_sorted=False)
    y1_ = f1(x1)
    delta_y = y1 - y1_
    
    mask=(delta_y>=(0.15 * y1_))
    y1_flt[mask] = 0
    y1_[~mask] = 0
    y1_flt += y1_

fig1 = plt.figure(figsize=(16, 9))
ax1 = fig1.add_subplot(111)
l1 = ax1.plot(x1, y1, c='skyblue', label='$\mathrm{Original~Spectra}$')
l2 = ax1.plot(x1, y1_flt, c='orange', alpha=0.8, label='$\mathrm{Filtered~Spectra}$')