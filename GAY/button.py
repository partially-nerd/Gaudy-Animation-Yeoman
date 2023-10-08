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
        alpha: int = 255,
        center: bool = True,
        visible: bool = True,
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
            alpha,
            center,
            visible,
        )
        self.text = text
        self.text_color = text_color
        self.canvas.btns.append(self)

        self.label = Label(
            self.canvas,
            self.text,
            (
                (self.canvas.w + self.x) / 2,
                (self.canvas.h + self.y) / 2,
            )
            if center
            else (self.x + self.w / 2, self.y + self.h / 2),
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


class Slider:
    def __init__(
        self,
        canvas,
        position: tuple[int] = (0, 550),
        slider_width: int = 200,
        max_value: float = 100,
    ) -> None:
        self.max_value = max_value
        self.slider_container = Rectangle(
            canvas,
            position,
            geometry=(slider_width, 10),
            background_color="#0e0e0e",
        )
        self.slider_label = Button(
            canvas,
            "",
            position=(
                self.slider_container.x - self.slider_container.w - 120,
                self.slider_container.y,
            ),
            background_color="#1a1a1a",
            border_width=0,
        )
        self.slider_child = Rectangle(
            canvas,
            (self.slider_container.x, self.slider_container.y),
            geometry=(20, 10),
            background_color="#e8502e",
            border_width=0,
        )

    def set_slider(
        self,
        property: str = "",
        value: float = 30,
    ):
        self.slider_child.x = value / self.max_value * self.slider_container.w
        self.slider_label.label.text = f"{property} = {round(value, 2)}"
