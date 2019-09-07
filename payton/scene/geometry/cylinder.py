import math
from typing import Any

from payton.scene.geometry import Mesh


class Cylinder(Mesh):
    """Cylinder Object

    Beware of using high values for number of meridians. You might end up with
    excessive number of vertices to render.

    Example use case:

        .. include:: ../../../examples/basics/18_cylinder.py

    """

    def __init__(
        self,
        bottom_radius: float = 0.5,
        top_radius: float = 0.5,
        meridians: int = 12,
        height: float = 1.0,
        **args: Any,
    ) -> None:
        """Iniitalize the cylinder

        Args:
          bottom_radius: Radius at the bottom of the cylinder
          top_radius: Radius at the top of the cylinder
          meridians: Number of meridians/edges (as in geography)
          height: Height of the cylinder
        """
        super().__init__(**args)
        self._bottom_radius: float = bottom_radius
        self._top_radius: float = top_radius
        self._meridians: int = meridians
        self._height: float = height
        self.build_cylinder()

    def build_cylinder(self) -> bool:
        step_angle = math.radians(360 / self._meridians)

        u_step = 1.0 / self._meridians
        r_bot = self._bottom_radius
        r_top = self._top_radius
        h_2 = self._height / 2.0
        for i in range(self._meridians):
            x1 = r_bot * math.cos(step_angle * i)
            y1 = r_bot * math.sin(step_angle * i)
            x2 = r_top * math.cos(step_angle * i)
            y2 = r_top * math.sin(step_angle * i)

            u1 = u_step * i
            v1 = 1.0
            u2 = u1
            v2 = 0.0

            x3 = r_bot * math.cos(step_angle * (i + 1))
            y3 = r_bot * math.sin(step_angle * (i + 1))
            x4 = r_top * math.cos(step_angle * (i + 1))
            y4 = r_top * math.sin(step_angle * (i + 1))

            u3 = u_step * (i + 1)
            v3 = 1.0
            u4 = u3
            v4 = 0.0

            self.add_triangle(
                [[x1, y1, -h_2], [x3, y3, -h_2], [x2, y2, h_2]],
                texcoords=[[u1, v1], [u3, v3], [u2, v2]],
            )

            self.add_triangle(
                [[x3, y3, -h_2], [x4, y4, h_2], [x2, y2, h_2]],
                texcoords=[[u3, v3], [u4, v4], [u2, v2]],
            )

            self.add_triangle(
                [[x1, y1, -h_2], [0.0, 0.0, -h_2], [x3, y3, -h_2]],
                texcoords=[[u1, v1], [0.0, 0.0], [u3, v3]],
            )

            self.add_triangle(
                [[x4, y4, h_2], [0.0, 0.0, h_2], [x2, y2, h_2]],
                texcoords=[[u4, v4], [0.0, 0.0], [u2, v2]],
            )

        self.fix_normals()
        return True