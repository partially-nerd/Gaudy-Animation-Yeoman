from pygame.draw import line
from pygame import Rect, Surface
from pygame import SRCALPHA
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
        alpha: int = 255,
        center: bool = True,
        visible: bool = True,
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
        self.alpha = alpha
        self.center = center
        self.visible = visible

    def update(self):
        if not self.visible:
            self.alpha = 0
            return

        if not self.center:
            rect_ = (
                self.x,
                self.y,
                self.h,
                self.h,
            )
        else:
            rect_ = (
                (self.canvas.w + self.x - self.h) / 2,
                (self.canvas.h + self.y - self.h) / 2,
                self.h,
                self.h,
            )

        surface = Surface(Rect(rect_).size, SRCALPHA)
        c = self.h / 2
        self.x_axis = line(
            surface,
            self.x_axis_color,
            (self.x, self.y + c),
            (self.x + self.h, self.y + c),
        )
        self.y_axis = line(
            surface,
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
                surface,
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

        surface.set_alpha(self.alpha)
        self.canvas.canvas.blit(surface, rect_)
