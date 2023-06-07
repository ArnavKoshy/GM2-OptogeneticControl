import numpy as np
import matplotlib.pyplot as plt
import scipy
from LightModel import calculate_intensity
# Define parameters

# Absorption coefficient of bacteria in fluid
mu = 2.0

# Position of light
light_pos = np.array([0,-1])

# Normalised direction of light
light_dir = np.array([0,1])

light_dir = light_dir / np.linalg.norm(light_dir)

# Number of points to simulate
N = 1000

# Generate a set of points in a circle
# Sqrt of r to ensure uniform distribution in r
rs = np.sqrt(np.random.rand(N))
thetas = np.random.rand(N) * 2 * np.pi

# Convert r, theta points to x,y for easier maths
xs = rs * np.cos(thetas)
ys = rs * np.sin(thetas)


# Convert to array of coords [[x0,y0],[x1,y1]....]
coords = np.dstack((xs, ys))
coords = coords[0]

# Calculate intensity
intensity = calculate_intensity(coords, light_pos=light_pos, light_dir=light_dir, mu=mu)


# Polar coordinates of points calculated
polar = np.dstack((rs, thetas))[0]
# Nearest neighbour interpolation/extrapolation (other 2D interpolators do not allow extrapolation)
intensity_interp = scipy.interpolate.NearestNDInterpolator(polar, intensity)

# Points to plot for line plot
rs_to_plot = np.ones(100)
thetas_to_plot = np.linspace(0, 2* np.pi, 100)

interped_intensity = intensity_interp(rs_to_plot, thetas_to_plot)

plt.plot(thetas_to_plot, interped_intensity)
plt.xlabel("Angulare position (rad)")
plt.ylabel("Intensity")
# Distribution heatmap
plt.figure()

# Set of points to plot
thetas_to_interp = np.linspace(0, 2* np.pi, 500)
rs_to_interp = np.sqrt(np.linspace(0,1,500))
# Convert to grid
grid_r, grid_theta = np.meshgrid(rs_to_interp, thetas_to_interp)

# Calculate values and plot data
data = intensity_interp(grid_r, grid_theta)
ax = plt.subplot(projection="polar")
ax.pcolormesh(thetas_to_interp,rs_to_interp, np.log(data.T), cmap="magma")
plt.show()
