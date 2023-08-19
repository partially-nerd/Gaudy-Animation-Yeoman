from pygame.draw import rect, circle, arc, polygon, line
from pygame import Rect, Surface
from pygame import SRCALPHA


class Rectangle:
    def __init__(
        self,
        canvas,
        position: tuple[int] = (0, 0),
        geometry: tuple[int] = (100, 50),
        background_color: str = "#0c0c0c",
        border_radius: int = 4,
        border_width: int = 2,
        border_color: str = "#eb4034",
        alpha: int = 255,
        center: bool = True,
        visible: bool = True,
    ):
        self.canvas = canvas
        self.canvas.elements.append(self)
        self.x, self.y = position
        self.w, self.h = geometry
        self.background_color = background_color
        self.border_radius = border_radius
        self.bw = border_width
        self.br_color = border_color
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
                self.w,
                self.h,
            )
        else:
            rect_ = (
                (self.canvas.w + self.x - self.w) / 2,
                (self.canvas.h + self.y - self.h) / 2,
                self.w,
                self.h,
            )
        surface = Surface(Rect(rect_).size, SRCALPHA)
        rect(
            surface,
            self.br_color,
            surface.get_rect(),
            border_radius=self.border_radius,
        )
        surface.set_alpha(self.alpha)
        self.canvas.canvas.blit(surface, rect_)
        if not self.center:
            rect_ = (
                self.x + self.bw,
                self.y + self.bw,
                self.w - 2 * self.bw,
                self.h - 2 * self.bw,
            )
        else:
            rect_ = (
                (self.canvas.w + self.x - self.w) / 2 + self.bw,
                (self.canvas.h + self.y - self.h) / 2 + self.bw,
                self.w - 2 * self.bw,
                self.h - 2 * self.bw,
            )
        surface = Surface(Rect(rect_).size, SRCALPHA)
        rect(
            surface,
            self.background_color,
            surface.get_rect(),
            border_radius=self.border_radius,
        )
        surface.set_alpha(self.alpha)
        self.canvas.canvas.blit(surface, rect_)


class Circle:
    def __init__(
        self,
        canvas,
        position: tuple[int] = (0, 0),
        radius: int = 25,
        background_color: str = "#0c0c0c",
        border_radius: int = 4,
        border_width: int = 2,
        border_color: str = "#eb4034",
        alpha: int = 255,
        center: bool = True,
        visible: bool = True,
    ):
        self.canvas = canvas
        self.canvas.elements.append(self)
        self.x, self.y = position
        self.r = radius
        self.background_color = background_color
        self.border_radius = border_radius
        self.bw = border_width
        self.br_color = border_color
        self.alpha = alpha
        self.center = center
        self.visible = visible

    def update(self):
        if not self.visible:
            self.alpha = 0
            return

        if not self.center:
            center = self.x, self.y
        else:
            center = (self.canvas.w + self.x) / 2, (self.canvas.h + self.y) / 2

        target_rect = Rect(center, (0, 0)).inflate((self.r * 2, self.r * 2))

        shape_surf = Surface(target_rect.size, SRCALPHA)
        circle(shape_surf, self.br_color, (self.r, self.r), self.r)
        shape_surf.set_alpha(self.alpha)
        self.canvas.canvas.blit(shape_surf, target_rect)

        shape_surf = Surface(target_rect.size, SRCALPHA)
        circle(shape_surf, self.background_color, (self.r, self.r), self.r - self.bw)
        shape_surf.set_alpha(self.alpha)
        self.canvas.canvas.blit(shape_surf, target_rect)
