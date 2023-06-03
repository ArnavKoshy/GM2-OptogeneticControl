import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys
from tqdm import tqdm
mu = 0.5
N = 5000
ax = plt.gca()
ax.set_aspect("equal")

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

intensity_pass1 = attenuation(dist)


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
            factor = np.abs(np.dot(vec/d, ray_dir)) * att / N
            intensity_pass2[i] += intensity_pass1[j] * factor

print(intensity_pass1)
print(intensity_pass2)

colors1 = magma(intensity_pass1/2)
colors2 = magma(intensity_pass2/2)

np.save("xs", xs)
np.save("ys", ys)
np.save("pass2", intensity_pass2)
sys.exit()
plt.title("Pass 1")
plt.axis('off')
plt.scatter(xs, ys, c=colors1, cmap="magma")
plt.figure()
ax = plt.gca()
ax.set_aspect("equal")
plt.axis('off')
plt.title("Pass 2")
plt.scatter(xs, ys, c=colors2, cmap="magma")
plt.show()
