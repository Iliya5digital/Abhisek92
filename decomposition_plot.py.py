import cartopy.crs as ccrs
import cartopy
import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar
import geemap
import rasterio
import ee
import geemap
import os
import shutil
import numpy as np
import pandas as pd
import glob2
import imageio
from rasterio.plot import reshape_as_raster, reshape_as_image
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, gamma, f, chi2
from astropy.convolution import convolve as ap_convolve
from astropy.convolution import Box2DKernel

ee.Authenticate()

ee.Initialize()

lat = -70.53611
lon = 24.04528
rectangle = ee.Geometry.Rectangle([lon - 0.06, lat - 0.06, lon + 0.06, lat + 0.06])
im1 = (ee.ImageCollection('COPERNICUS/S1_GRD') 
                       .filterBounds(rectangle)
                       .filterDate(ee.Date('2021-12-01'), ee.Date('2022-01-31'))
                       .filter(ee.Filter.eq('orbitProperties_pass', 'ASCENDING'))
                       .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'HH'))
                       .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'HV'))
                       .filter(ee.Filter.eq('relativeOrbitNumber_start', 132))
                       )

out_dir = '/content/drive/MyDrive/s1'
filename = os.path.join(out_dir, 's1a.tif')
#geemap.ee_export_image(im1.select(['HH', 'HV', 'angle']), filename=filename, scale=10, region=rectangle, crs='EPSG:3031', file_per_band=False)
geemap.ee_export_image_collection(im1, out_dir=out_dir, scale=10, region=rectangle, crs='EPSG:3031', file_per_band=False)

out_dir = '/content/drive/MyDrive/s1'
filelist2 = glob2.glob(out_dir+'/S1*tif')
filelist = filelist2[0:20]
i = filelist[0]
date = i[49:51] + '-' + i[47:49] + '-' + i[43:47]

for i in filelist:
  date = i[49:51] + '-' + i[47:49] + '-' + i[43:47]
  dataset = rasterio.open(i)
  bands = dataset.read((1,2))
  # image = reshape_as_image(bands)
  # bands_1 = dataset.read()
  # image_1 = reshape_as_image(bands_1)

  #gamma_hh = image_1[:, :, 0] / np.cos(image_1[:, :, 2] * 0.01745329251)
  #gamma_hv = image_1[:, :, 1] / np.cos(image_1[:, :, 2] * 0.01745329251)

# Valid Pixel Mask 

  valid_mask = np.logical_not(
      np.logical_and(
          (bands[0, :, :] > image[1, :, :]), 
          (image[0, :, :] > -20)
        )
    )
    vm2 = np.stack((valid_mask, valid_mask), 0)

  image1 = np.ma.masked_array(image, vm2, fill_value=np.nan)

# dB to Linear conversion

  lin_hh = 10.0 ** (image1[0,:,:] / 10.0)
  lin_hv = 10.0 ** (image1[1,:,:] / 10.0)

  # lin_hh = 10.0 ** (gamma_hh / 10.0)
  # lin_hv = 10.0 ** (gamma_hv / 10.0)

# 5 x 5 Boxcar filter for speckle removal

  box_kernel = Box2DKernel(5)
  hh = ap_convolve(lin_hh, box_kernel, normalize_kernel=True)
  hv = ap_convolve(lin_hv, box_kernel, normalize_kernel=True)

# Dual Polarimetric indicators

  q = lin_hv / lin_hh
  x = (1 - q)
  y = (1 + q)
  m_c = x / y
  theta_c = np.rad2deg(np.arctan((x ** 2) / (x + (q ** 2))))
  p1 = 1 / y
  p2 = q * p1
  h_c = -(p1 * np.log2(p1)) - (p2 * np.log2(p2))
  
  mask = np.logical_not(np.logical_and(np.isfinite(h_c), np.isfinite(theta_c)))
  mask = np.logical_and(valid_mask, mask)
  
  h_c = np.ma.masked_array(h_c, mask, fill_value=np.nan)
  theta_c = np.ma.masked_array(theta_c, mask, fill_value=np.nan)

# H_c / Theta_c Classification Plane

  z1_mask = np.logical_and((np.logical_and((0 <= h_c), (h_c < 0.3))), np.logical_and((30<= theta_c), (theta_c <= 45)))
  z2_mask = np.logical_and((np.logical_and((0.3 <= h_c), (h_c < 0.5))), np.logical_and((30<= theta_c), (theta_c <= 45)))
  z3_mask = np.logical_and((np.logical_and((0.5 <= h_c), (h_c < 0.7))), np.logical_and((30<= theta_c), (theta_c <= 45)))
  z4_mask = np.logical_and((np.logical_and((0.7 <= h_c), (h_c <= 1))), np.logical_and((30<= theta_c), (theta_c <= 45)))
  z5_mask = np.logical_and((np.logical_and((0.7 <= h_c), (h_c <= 1))), np.logical_and((15<= theta_c), (theta_c < 30)))
  z6_mask = np.logical_and((np.logical_and((0.7 <= h_c), (h_c <= 1))), np.logical_and((0<= theta_c), (theta_c < 15)))
  z0_mask = np.logical_and((np.logical_and((0 <= h_c), (h_c < 0.7))), np.logical_and((0<= theta_c), (theta_c < 30)))

  r = np.zeros(h_c.shape).astype(np.uint8)
  g = np.zeros(h_c.shape).astype(np.uint8)
  b = np.zeros(h_c.shape).astype(np.uint8)

  r[z1_mask] = 255
  r[z2_mask] = 125 
  r[z3_mask] = 0
  r[z4_mask] = 255
  r[z5_mask] = 0
  r[z6_mask] = 0
  r[z0_mask] = 127

  g[z1_mask] = 5
  g[z2_mask] = 27 
  g[z3_mask] = 255
  g[z4_mask] = 213
  g[z5_mask] = 255
  g[z6_mask] = 102
  g[z0_mask] = 127

  b[z1_mask] = 180
  b[z2_mask] = 96
  b[z3_mask] = 34
  b[z4_mask] = 113
  b[z5_mask] = 255
  b[z6_mask] = 5
  b[z0_mask] = 127
  
  msk = np.logical_or(np.logical_and.reduce((z0_mask, z1_mask, z2_mask, z3_mask, z4_mask, z5_mask, z6_mask)))
  mask = np.logical_and(mask, msk)

  rgb = np.stack((r, g, b), -1)
  rgb = np.ma.masked_array(rgb, np.stack(((mask,) * 3), -1), fill_value=255)


# Plotting 

  plt.figure(figsize=(15,15))

  ax1 = plt.subplot(131)
  ax1.imshow(theta_c, cmap= 'jet', origin='upper')
  plt.text(0.5, 0.02, date, horizontalalignment='center', verticalalignment='bottom', transform=ax1.transAxes,size=25, color='black', weight='bold')
  scalebar = ScaleBar(1,box_alpha=0,color='black',location='lower left')
  ax1.add_artist(scalebar)

  ax2 = plt.subplot(132)
  ax2.imshow(h_c, cmap= 'jet', origin='upper')
  plt.text(0.5, 0.02, date, horizontalalignment='center', verticalalignment='bottom', transform=ax2.transAxes,size=25, color='black', weight='bold')
  scalebar = ScaleBar(1,box_alpha=0,color='black',location='lower left')
  ax2.add_artist(scalebar)

  ax3 = plt.subplot(133)
  ax3.imshow(rgba, cmap= 'jet', origin='upper')
  plt.text(0.5, 0.02, date, horizontalalignment='center', verticalalignment='bottom', transform=ax3.transAxes,size=25, color='black', weight='bold')
  scalebar = ScaleBar(1,box_alpha=0,color='black',location='lower left')
  ax3.add_artist(scalebar)