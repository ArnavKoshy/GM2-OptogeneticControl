import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from LightModel import calculate_intensity


mu = 0.1
N = 1000

# Generate random points in 3D
rs = np.sqrt(np.random.rand(N))
thetas = np.random.rand(N) * 2 * np.pi
xs = rs * np.sin(thetas)
ys = rs * np.cos(thetas)
zs = np.random.rand(N) * 2 - 1

coords = np.dstack((xs, ys,zs))
coords = coords[0]

light_pos = np.array([0,-1,0])

intensity = calculate_intensity(coords, light_dir=-light_pos, light_pos=light_pos, mu=mu)

magma = matplotlib.colormaps.get_cmap("magma")
colors = magma(intensity)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.scatter(xs, ys, zs, c=colors)
plt.show()



