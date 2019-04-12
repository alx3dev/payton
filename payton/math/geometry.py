import numpy as np
import pyrr

def point_project(p, origin, direction):
    return (direction[0] * (p[0] - origin[0]) +
            direction[1] * (p[1] - origin[1]) +
            direction[2] * (p[2] - origin[2]))

def distance(v1, v2):
    v3 = v2 - v1
    return pyrr.vector3.length(v3)

def distance2(v1, v2):
    v3 = v2 - v1
    return (pyrr.vector3.length(v3) ** 2)

def combine(v1, v2, f1, f2):
    x = (f1 * v1[0]) + (f2 * v2[0])
    y = (f1 * v1[1]) + (f2 * v2[1])
    z = (f1 * v1[2]) + (f2 * v2[2])
    w = (f1 * v1[3]) + (f2 * v2[3])
    return np.array([x, y, z, w], dtype=np.float32)

def raycast_sphere_intersect(start, vector, sphere_center, sphere_radius):
    """Raycast Sphere Intersect Test

    Args:
      start: Start of the ray
      vector: Vector (direction) of the ray
      sphere_center: Sphere center in global coordinates
      sphere_radius: Sphere radius

    Returns:
      bool
    """
    proj = point_project(sphere_center, start, vector)
    if proj < 0:
        proj = 0.0
    vc = combine(start, vector, 1.0, proj)
    dist = distance2(sphere_center, vc)
    return dist < (sphere_radius ** 2)
    