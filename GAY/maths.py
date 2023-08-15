from pygame.draw import line
import math


class Graph:
    def __init__(
        self,
        canvas,
        position: tuple[int] = (0, 0),
        height: int = 300,
        axis_colors: tuple[str] = ("#6290a6", "#eb4034"),
        graph=lambda x: x**2,
        graph_color: str = "#5bff42",
        range_: tuple = (-10, 10),
        resolution: int = 0.5,
    ) -> None:
        self.canvas = canvas
        self.canvas.elements.append(self)
        self.x, self.y = position
        self.h = height
        self.x_axis_color, self.y_axis_color = axis_colors
        self.fn = graph
        self.color = graph_color
        self.l_limit, self.u_limit = range_
        self.res = resolution

    def update(self):
        c = self.h / 2
        self.x_axis = line(
            self.canvas.canvas,
            self.x_axis_color,
            (self.x, self.y + c),
            (self.x + self.h, self.y + c),
        )
        self.y_axis = line(
            self.canvas.canvas,
            self.y_axis_color,
            (self.x + c, self.y),
            (self.x + c, self.y + self.h),
        )
        x1 = self.l_limit
        v = self.h / (self.u_limit - self.l_limit)
        cx = self.x + c
        cy = self.y + c
        while self.l_limit <= x1 <= self.u_limit:
            x2 = x1 + self.res
            line(
                self.canvas.canvas,
                self.color,
                (
                    cx - x1 * v,
                    cy - self.fn(-x1) * v,
                ),
                (
                    cx - x2 * v,
                    cy - self.fn(-x2) * v,
                ),
            )
            x1 += self.res
