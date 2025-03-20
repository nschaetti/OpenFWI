

# Imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from rich.traceback import install


# Traceback
install()


# Load data and label visualisation
velocity = np.load('data/FlatVel_A/model/model1.npy')
data = np.load('data/FlatVel_A/data/data1.npy')

# SHow sizes
print(f"Velocity shape: {velocity.shape}")
print(f"Data shape: {data.shape}")

# Velocity Map Visualisation
sample = 14
rainbow_cmap = ListedColormap(np.load('rainbow256.npy'))
fix, ax = plt.subplots(1, 1, figsize=(11, 5))
img = ax.imshow(velocity[sample,0,:,:])
ax.set_xticks(range(0, 70, 10))
ax.set_xticklabels(range(0, 700, 100))
ax.set_yticks(range(0, 70, 10))
ax.set_yticklabels(range(0, 700, 100))
ax.set_ylabel('Depth (m)', fontsize=12)
ax.set_xlabel('Offset (m)', fontsize=12)
clb=plt.colorbar(img, ax=ax)
clb.ax.set_title('km/s', fontsize=8)
plt.show()

# Check seismic
print('Seismic data size:', data.shape)

fig, ax = plt.subplots(1, 5, figsize=(20, 5))

ax[0].imshow(data[sample, 0, :, :], extent=[0, 70, 1000, 0], aspect='auto', cmap='gray', vmin=-0.5, vmax=0.5)
ax[1].imshow(data[sample, 1, :, :], extent=[0, 70, 1000, 0], aspect='auto', cmap='gray', vmin=-0.5, vmax=0.5)
ax[2].imshow(data[sample, 2, :, :], extent=[0, 70, 1000, 0], aspect='auto', cmap='gray', vmin=-0.5, vmax=0.5)
ax[3].imshow(data[sample, 3, :, :], extent=[0, 70, 1000, 0], aspect='auto', cmap='gray', vmin=-0.5, vmax=0.5)
ax[4].imshow(data[sample, 4, :, :], extent=[0, 70, 1000, 0], aspect='auto', cmap='gray', vmin=-0.5, vmax=0.5)

for axis in ax:
    axis.set_xticks(range(0, 70, 10))
    axis.set_xticklabels(range(0, 700, 100))
    axis.set_yticks(range(0, 2000, 1000))
    axis.set_yticklabels(range(0, 2, 1))
    axis.set_ylabel('Time (s)', fontsize=12)
    axis.set_xlabel('Offset (m)', fontsize=12)
# end for

plt.show()
