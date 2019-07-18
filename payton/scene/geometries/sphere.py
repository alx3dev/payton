import math
from typing import Any

from payton.scene.geometries.mesh import Mesh
from payton.math.vector import plane_normal


class Sphere(Mesh):
    """
    Sphere object.

    This object is generated using basic Spherical coordinates.
    Beware of using high values for parallels and meridians. You might end up
    with excessive number of vertices to render and a performance trouble.

    Parameters:

    - `radius` default: `0.5`
    - `parallels` default: `12`
    - `meridians` default: `12`

    Sphere object use case

        .. include:: ../../../examples/basics/05_children.py

    """

    def __init__(self, **args: Any) -> None:
        """Initialize the sphere

        Args:
          radius: Radius of the sphere (default: 0.5, making it a unit sphere)
          parallels: Number of parallels (as in geography). (default: 12, 30
                     degrees of arcs)
          meridians: Number of meridians (as in geography). (default: 12)
        """
        super().__init__(**args)
        self.radius: float = args.get("radius", 0.5)
        self.parallels: int = args.get("parallels", 12)
        self.meridians: int = args.get("meridians", 12)
        self.build_sphere()

    def build_sphere(self) -> bool:
        """
        Generate the sphere

        Returns:
          bool: `True` on successful creation of a `Sphere` object.
        """
        r = self.radius
        # step angle is the rotational angle to build the sphere
        step_angle = math.radians(360.0 / self.meridians)
        # step height is the arc in height
        step_height = math.radians(180.0 / self.parallels)
        indices = 0
        u_step = 1.0 / self.meridians
        v_step = 1.0 / self.parallels

        for i in range(self.parallels):
            for j in range(self.meridians):
                x1 = r * math.sin(step_height * i) * math.cos(step_angle * j)
                y1 = r * math.sin(step_height * i) * math.sin(step_angle * j)
                z1 = r * math.cos(step_height * i)
                u1 = u_step * j
                v1 = v_step * i

                x2 = (
                    r
                    * math.sin(step_height * (i + 1))
                    * math.cos(step_angle * j)
                )
                y2 = (
                    r
                    * math.sin(step_height * (i + 1))
                    * math.sin(step_angle * j)
                )
                z2 = r * math.cos(step_height * (i + 1))
                u2 = u_step * j
                v2 = v_step * (i + 1)

                x3 = (
                    r
                    * math.sin(step_height * (i + 1))
                    * math.cos(step_angle * (j + 1))
                )
                y3 = (
                    r
                    * math.sin(step_height * (i + 1))
                    * math.sin(step_angle * (j + 1))
                )
                z3 = r * math.cos(step_height * (i + 1))
                u3 = u_step * (j + 1)
                v3 = v_step * (i + 1)

                x4 = (
                    r
                    * math.sin(step_height * i)
                    * math.cos(step_angle * (j + 1))
                )
                y4 = (
                    r
                    * math.sin(step_height * i)
                    * math.sin(step_angle * (j + 1))
                )
                z4 = r * math.cos(step_height * i)
                u4 = u_step * (j + 1)
                v4 = v_step * i

                normal = plane_normal([x1, y1, z1], [x2, y2, z2], [x3, y3, z3])
                self._vertices.append([x1, y1, z1])
                self._vertices.append([x2, y2, z2])
                self._vertices.append([x3, y3, z3])
                self._vertices.append([x4, y4, z4])
                self._texcoords.append([u1, v1])
                self._texcoords.append([u2, v2])
                self._texcoords.append([u3, v3])
                self._texcoords.append([u4, v4])
                self._normals.append([normal[0], normal[1], normal[2]])
                self._normals.append([normal[0], normal[1], normal[2]])
                self._normals.append([normal[0], normal[1], normal[2]])
                self._normals.append([normal[0], normal[1], normal[2]])
                self._indices.append([indices, indices + 1, indices + 2])
                self._indices.append([indices, indices + 2, indices + 3])
                indices += 4
        return True