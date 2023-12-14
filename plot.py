from mpl_toolkits.mplot3d import Axes3D
import cmocean.cm as cmo
from matplotlib.path import Path
import matplotlib.patches as patches
from matplotlib import pyplot as plt
import numpy as np
from numpy import polyfit, polyval

q = np.linspace(0.0000001, 0.9999999, num=10000)
x = (1 - q) # 1 - ratio
y = (1 + q) # 1 + ratio
theta_c = np.rad2deg(np.arctan((x ** 2) / (x + (q ** 2)))) #theta_c
p1 = 1 / y # 1 / y
p2 = q * p1 # p1 * ratio
h_c = -(p1 * np.log2(p1)) - (p2 * np.log2(p2)) #h_c
alpha = np.rad2deg(np.arctan((theta_c / 45) / h_c))

# xx, yy = np.meshgrid(h_c, theta_c)
params = polyfit(h_c, theta_c, 8, full=False, cov=False)
def fun(dat):
    return polyval(params, dat)

xx = np.linspace(0, 1, 1000)
yy = np.linspace(0, 1, 1000)
xx, yy = np.meshgrid(xx, yy)
zz = np.arctan2(xx, yy) / (2 * np.pi)
zz[(45*yy)>fun(xx)] = np.nan
# dd = zz - yy
# dd[yy>zz] = np.nan
# dd = -dd

z1_mask = np.logical_and((np.logical_and((0 <= h_c), (h_c < 0.3))), np.logical_and((30<= theta_c), (theta_c <= 45)))
z2_mask = np.logical_and((np.logical_and((0.3 <= h_c), (h_c < 0.5))), np.logical_and((30<= theta_c), (theta_c <= 45)))
z3_mask = np.logical_and((np.logical_and((0.5 <= h_c), (h_c < 0.7))), np.logical_and((30<= theta_c), (theta_c <= 45)))
z4_mask = np.logical_and((np.logical_and((0.7 <= h_c), (h_c <= 1))), np.logical_and((30<= theta_c), (theta_c <= 45)))
z5_mask = np.logical_and((np.logical_and((0.7 <= h_c), (h_c <= 1))), np.logical_and((15<= theta_c), (theta_c < 30)))
z6_mask = np.logical_and((np.logical_and((0.7 <= h_c), (h_c <= 1))), np.logical_and((0<= theta_c), (theta_c < 15)))
z0_mask = np.logical_and((np.logical_and((0 <= h_c), (h_c < 0.7))), np.logical_and((0<= theta_c), (theta_c < 30)))

fig = plt.figure(figsize=(10,10))
ax = plt.subplot(1, 1, 1)
ax.plot(h_c[z1_mask], theta_c[z1_mask], linewidth=7, color='#fde725')
ax.plot(h_c[z2_mask], theta_c[z2_mask], linewidth=7, color='#7ad151')
ax.plot(h_c[z3_mask], theta_c[z3_mask], linewidth=7, color='#22a884')
ax.plot(h_c[z4_mask], theta_c[z4_mask], linewidth=7, color='#2a788e')
ax.plot(h_c[z5_mask], theta_c[z5_mask], linewidth=7, color='#414487')
ax.plot(h_c[z6_mask], theta_c[z6_mask], linewidth=7, color='#440154')

# c = ax.pcolormesh(h_c, theta_c, distances, shading='auto', cmap='viridis', alpha=0.7)
c = ax.imshow(zz, extent=(0, 1, 0, 45), aspect='auto', origin='lower', cmap=cmo.ice_r)

ax.plot([0, 0.765], [0, 32], color='red', linewidth=2, linestyle='-')
ax.plot([0, 1], [0, 0], color='red', linewidth=2, linestyle='-')

plt.ylim([0, 45])
plt.xlim([0, 1])
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
ax.set_ylabel(r'$\theta_c$ [deg]', fontsize=20)
ax.set_xlabel('$H_c$', fontsize=20)
plt.savefig("foo.png")