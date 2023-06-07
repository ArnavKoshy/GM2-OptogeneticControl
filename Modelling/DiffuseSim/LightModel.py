from tqdm import tqdm
import numpy as np


def calculate_intensity(coords, light_pos = np.array([0,-1]), light_dir = np.array([0,1]), mu = 0.1):
    """Calculate intensities of light in a turbid medium at a set of discrete points

    Args:
        coords (np.array): A array of [x,y] coordinates of the points
        light_pos (np.array, optional): position of light in 3D space. Defaults to np.array([0,-1]).
        light_dir (np.array, optional): direction vectorof light. Defaults to np.array([0,1]).
        mu (float, optional): Absorption coefficient of fluid. Defaults to 0.1.

    Returns:
        _type_: _description_
    """

    light_dir = light_dir / np.linalg.norm(light_dir)
    # Beer-Lambert law for attenuation - https://en.wikipedia.org/wiki/Beer%E2%80%93Lambert_law
    attenuation = lambda length: np.exp(-1 * mu * length)


    # Displacement of each point from light (used for attenuation)
    disp = coords - light_pos
    # print(disp.shape)
    # Distance of each point from light
    dist_sqrd = (disp * disp).sum(axis=1)
    dist = np.sqrt(dist_sqrd)

    # Normalise each displacement vector to later calculate angle between light direction and displacement
    dist_stack = np.dstack([dist] * disp.shape[1])[0]
    disp_normalised = disp/dist_stack


    # Calculate dot products of displacement of a point and light direction (in this case equal to cosine of angle)
    dots = np.sum(disp_normalised * light_dir, axis=1)

    # Angles if a different light distribution is to be implemented
    # e.g light_distribution_factor = 1 / (1 + angles_to_lights**2)
    # angles_to_light = np.arccos(dots)

    light_distribution_factor = dots


    N = len(dist)
    # Calculate initial intensity due to direct lighting - attenuation due to fluid and light distribution
    intensity_pass1 = attenuation(dist) * light_distribution_factor / np.sqrt(N)


    # Copy data to add to it
    intensity_pass2 = intensity_pass1.copy()

    # For each point (target)
    for i in tqdm(range(N)):
        # For each other point (illuminator)
        for j in range(N):
            if i!=j:

                # Distance & displacement from illuminator
                vec = coords[i] - coords[j]
                d = np.linalg.norm(vec)

                # Attenuation due to distance
                att = attenuation(d)
                # Normalised ray direction to illuminator
                ray_dir = coords[j] - light_pos
                ray_dir /= np.linalg.norm(ray_dir)

                # Dot product of displacement w.r.t ray direction used
                # to calculate cosine of angle
                # 
                dot = np.dot(vec/d, ray_dir)

                # Use to calculate other scattering functions
                # angle_to_target= np.arccos(dot)

                # Factor of incident light on illuminator that is transferred to target
                factor = 0

                # If target is in front of the illuminator w.r.t ray (no back scattering)
                # and not directly in front of the illuminator (this is accounted for with B-L)
                # It's assumed pockets scatter light proportional to their volume - bigger points scatter more
                if(dot > 0 and dot < 1):
                    factor = dot * att / np.sqrt(N)

                # Add intensity from illuminator to target
                intensity_pass2[i] += intensity_pass1[j] * factor

    return intensity_pass2