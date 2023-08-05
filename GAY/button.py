from pygame.draw import rect
from .label import Label
from .shapes import Rectangle


class Button(Rectangle):
    def __init__(
        self,
        canvas,
        text: str = "+",
        position: tuple[int] = (0, 0),
        geometry: tuple[int] = (50, 50),
        background_color: str = "#0c0c0c",
        text_color: str = "#ffffff",
        border_radius: int = 4,
        border_width: int = 2,
        border_color: str = "#6290a6",
    ):
        super().__init__(
            canvas,
            position,
            geometry,
            background_color,
            border_radius,
            border_width,
            border_color,
        )
        self.text = text
        self.text_color = text_color
        self.canvas.btns.append(self)

        self.label = Label(
            self.canvas,
            self.text,
            (self.x + self.w / 2, self.y + self.h / 2),
            self.text_color,
            self.background_color,
        )

    def onclick(self):
        print("Hello, Nerd!")

    def check_click(self, mouse):
        if (
            self.x <= mouse[0] <= self.w + self.x
            and self.y <= mouse[1] <= self.h + self.y
        ):
            self.onclick()
