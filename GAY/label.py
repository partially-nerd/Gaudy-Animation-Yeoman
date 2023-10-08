class Label:
    def __init__(
        self,
        canvas,
        text: str,
        position: tuple[int] = (0, 0),
        text_color: str = "#ffffff",
        background_color: str = "#000000",
    ) -> None:
        self.canvas = canvas
        self.canvas.elements.append(self)
        self.text_color = text_color
        self.text = text
        self.x, self.y = position
        self.background_color = background_color

    def update(self):
        text = self.canvas.font.render(
            self.text, self.text_color, self.background_color
        )
        text_rect = text[1]

        text_rect.center = self.x, self.y
        self.canvas.canvas.blit(text[0], text_rect)
