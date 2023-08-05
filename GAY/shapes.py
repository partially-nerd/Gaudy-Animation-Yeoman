from pygame.draw import rect, circle, arc, polygon, line


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
    ):
        self.canvas = canvas
        self.canvas.elements.append(self)
        self.x, self.y = position
        self.w, self.h = geometry
        self.background_color = background_color
        self.border_radius = border_radius
        self.bw = border_width
        self.br_color = border_color

    def update(self):
        self.rect = rect(
            self.canvas.canvas,
            self.background_color,
            (self.x, self.y, self.w, self.h),
            border_radius=self.border_radius,
        )
        rect(
            self.canvas.canvas,
            self.br_color,
            (self.x, self.y, self.w, self.h),
            border_radius=self.border_radius,
            width=self.bw,
        )


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
    ):
        self.canvas = canvas
        self.canvas.elements.append(self)
        self.x, self.y = position
        self.r = radius
        self.background_color = background_color
        self.border_radius = border_radius
        self.bw = border_width
        self.br_color = border_color

    def update(self):
        self.object = circle(
            self.canvas.canvas,
            self.background_color,
            (self.x + self.r, self.y + self.r),
            self.r,
        )
        circle(
            self.canvas.canvas,
            self.br_color,
            (self.x + self.r, self.y + self.r),
            self.r,
            width=self.bw,
        )
