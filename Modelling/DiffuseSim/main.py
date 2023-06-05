import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys
from tqdm import tqdm
import scipy
mu = 0.1
N = 1000


magma = matplotlib.colormaps.get_cmap("magma")

def attenuation(length):
    
    return np.exp(-1 * mu * length)

rs = np.sqrt(np.random.rand(N))
thetas = np.random.rand(N) * 2 * np.pi
xs = rs * np.sin(thetas)
ys = rs * np.cos(thetas)

coords = np.dstack((xs, ys))
coords = coords[0]


light_pos = np.array([0,-1])
disp = coords - light_pos

dist = np.sqrt((disp * disp).sum(axis=1))

dist_stack = np.dstack((dist, dist))[0]
disp_normalised = disp/dist_stack

dots = np.sum(disp_normalised * light_pos * -1, axis=1)
thetas_of_points = np.arccos(dots)
# atts = 1 / (1 + thetas_of_points * thetas_of_points * 10)
atts = dots
# atts = 1


intensity_pass1 = attenuation(dist) * atts


intensity_pass2 = intensity_pass1.copy()
for i in tqdm(range(N)):
    for j in range(N):
        if i!=j:
            # Distance from illuminator
            vec = coords[i] - coords[j]
            d = np.linalg.norm(vec)
            att = attenuation(d)
            # Normalised ray direction to illuminator
            ray_dir = coords[j] - light_pos
            ray_dir /= np.linalg.norm(ray_dir)
            dot = np.dot(vec/d, ray_dir)
            factor = 0
            if(dot > 0 ):
                factor = dot * att / N
            
            intensity_pass2[i] += intensity_pass1[j] * factor

print(intensity_pass1)
print(intensity_pass2)

colors1 = magma(intensity_pass1/2)
colors2 = magma(intensity_pass2/2)

# np.save("xs", xs)
# np.save("ys", ys)
# np.save("pass2", intensity_pass2)
# sys.exit()

interp2 = scipy.interpolate.NearestNDInterpolator(coords, intensity_pass2)
interp1 = scipy.interpolate.NearestNDInterpolator(coords, intensity_pass1)

polar = np.dstack((rs, thetas - np.pi))[0]
rinterp2 = scipy.interpolate.NearestNDInterpolator(polar, intensity_pass2)
rinterp1 = scipy.interpolate.NearestNDInterpolator(polar, intensity_pass1)
thetas_to_plot = np.linspace(0, 2* np.pi, 100)
xs_to_plot = np.cos(thetas_to_plot)
ys_to_plot = np.sin(thetas_to_plot)
zs1 = interp1(xs_to_plot, ys_to_plot)
zs2 = interp2(xs_to_plot, ys_to_plot)
# print(zs)
plt.plot(thetas_to_plot, np.roll(zs1, 25), label="Pass 1")
plt.plot(thetas_to_plot, np.roll(zs2, 25), label="Pass 2")
plt.legend()
plt.figure()
ax = plt.gca()
ax.set_aspect("equal")
plt.title("Pass 1")
plt.axis('off')
thetas_to_interp = np.linspace(-np.pi, np.pi, 500)
rs_to_interp = np.sqrt(np.linspace(0,1,500))
grid_r, grid_theta = np.meshgrid(rs_to_interp, thetas_to_interp)
data = rinterp2(grid_r, grid_theta)
ax1 = plt.subplot(projection="polar")
ax1.pcolormesh(thetas_to_interp,rs_to_interp,data.T, cmap="magma")
plt.show()
sys.exit()
# plt.scatter(xs, ys, c=colors1, cmap="magma")
# plt.figure()
ax = plt.gca()
ax.set_aspect("equal")
plt.axis('off')
plt.title("Pass 2")
plt.scatter(xs, ys, c=colors2, cmap="magma")
plt.show()
