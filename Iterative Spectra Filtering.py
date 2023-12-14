import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
 
from matplotlib import rc
rc('text', usetex=True, aa=True)
plt.rcParams.update({'font.size': 18})
plt.ion()

# Inputs
k_size = 3
max_iter = 20
 
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

i = 0
sd = np.inf

iters = list()
sdevs = list()
bdevs = list()

while i < max_iter:
    yy1 = np.convolve(y1_flt, np.ones((k_size,))/k_size, mode='valid')
    xx1 = np.convolve(x1_flt, np.ones((k_size,))/k_size, mode='valid')
 
    f1 = interp1d(x=xx1, y=yy1, kind='linear', fill_value="extrapolate", assume_sorted=False)
    y1_ = f1(x1)
    bdevs.append(np.std(y1_))
    delta_y = np.abs(y1 - y1_)
    
    # mask=(delta_y>=(0.15 * y1_))
    # y1_flt[mask] = 0
    
    mask= (delta_y < np.abs(0.15 * y1_))
    y1_[mask] = 0
    y1_flt += y1_
    y1_flt[np.logical_not(mask)] *= 0.5
    sd = np.std(y1_flt)
    i += 1

c_mask = y1==y1_flt
yc = y1[c_mask]
xc = x1[c_mask]

fig1 = plt.figure(figsize=(10, 10))
ax1 = fig1.add_subplot(111)
l1 = ax1.scatter(x1, y1, c='red', alpha=0.4, label='$\mathrm{Removed~points~from~Original~Spectra}$')
l2 = ax1.scatter(x1, y1_flt, c='blue', label='$\mathrm{Additional~Points~in~Filtered~Spectra}$')
l3 = ax1.scatter(xc, yc, c='green', label='$\mathrm{Overlapped~Points}$')
ax1.set_xlabel("$\mathrm{Wavelength}~(\mu)$")
ax1.set_ylabel("$\mathrm{Reflectance}$")
ax1.legend(loc=8)

input("Press Enter to continue...")
