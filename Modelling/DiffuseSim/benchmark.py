import numpy as np
import matplotlib.pyplot as plt
import scipy
from LightModel import calculate_intensity

mu = 1.7
N = 1250


Xs = np.linspace(-5,5, 50)
Ys = np.linspace(0,5,25)
X,Y = np.meshgrid(Xs,Ys)
coords = np.dstack([X.ravel(), Y.ravel()])[0]


light_pos = np.array([0,0])
light_dir = np.array([0,1])

intensity = calculate_intensity(coords, light_pos=light_pos, light_dir=light_dir, mu=mu)


interp = scipy.interpolate.LinearNDInterpolator(coords, intensity)
ax = plt.gca()
ax.set_aspect("equal")

xs = np.linspace(-5,5,500)
ys = np.linspace(0,5,500)
grid_x, grid_y = np.meshgrid(xs, ys)
data = interp(grid_x, grid_y)

plt.pcolormesh(ys, xs,data.T, cmap="jet")

plt.show()
