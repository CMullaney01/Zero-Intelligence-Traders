# Author: Johann Faouzi <johann.faouzi@gmail.com>
# License: BSD-3-Clause

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
from pyts.image import RecurrencePlot
from pyts.datasets import load_gunpoint
import numpy as np

# Load the GunPoint dataset
# X, _, _, _ = load_gunpoint(return_X_y=True)

# X is the array of X.csv file
X = np.genfromtxt('X.csv', delimiter=',')
X = X.reshape(1, -1)
# recurrence plot of 1 D array X
rp = RecurrencePlot(threshold='point', percentage=10)
# rp = RecurrencePlot()
X_rp = rp.fit_transform(X)

print(X_rp.shape)

# Get the recurrence plots for all the time series
# rp = RecurrencePlot(threshold='point', percentage=20)
# print(X)
# X_rp = rp.fit_transform(X)
# print(X_rp)


# Plot the 50 recurrence plots
fig = plt.figure(figsize=(1, 1))

grid = ImageGrid(fig, 111, nrows_ncols=(1, 1), axes_pad=0.1, share_all=True)
for i, ax in enumerate(grid):
    ax.imshow(X_rp[i], cmap='binary', origin='lower')
grid[0].get_yaxis().set_ticks([])
grid[0].get_xaxis().set_ticks([])

fig.suptitle(
    "Recurrence plots for the 50 time series in the 'GunPoint' dataset",
    y=0.1
)

plt.show()