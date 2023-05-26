from main import solve
from pygame import init, quit, QUIT, MOUSEBUTTONDOWN
from pygame.display import set_mode, flip
from pygame.time import Clock
from pygame.font import SysFont
from pygame.draw import rect
from pygame.mouse import get_pos
from pygame.event import get as get_events

class Button:
    def __init__(
            self, canvas, text: str = "+",
            pos: tuple[int] = (0, 0),
            geometry: tuple[int] = (50, 50),
            bg: str = "#000000",
        ):
        self.canvas = canvas
        self.canvas.btns.append(self)
        self.x, self.y = pos
        self.w, self.h = geometry
        self.bg = bg
    def onclick(self):
        print("hi")
    def check_click(self, mouse):
        if self.x <= mouse[0] <= self.w + self.x and self.y <= mouse[1] <= self.h + self.y:
            self.onclick()
    def update(self):
        self.object = rect(self.canvas.canvas, self.bg, (self.x, self.y, self.w, self.h))

class Window:
    running: bool = True
    fps: int = 60
    btns: list = []
    def __init__(self, geometry: tuple[int]) -> None:
        init()
        self.font = SysFont('Corbel',35)
        self.canvas = set_mode(geometry)
        self.clock = Clock()
    def run(self):
        while self.running:
            for event in get_events():
                if event.type == QUIT:
                    self.running = False
                elif event.type == MOUSEBUTTONDOWN:
                    mouse = get_pos()
                    for btn in self.btns:
                        btn.check_click(mouse)
            self.canvas.fill("#1a1a1a")
            self.update()
            flip()
            self.clock.tick(self.fps)
        quit()
    def update(self):
        for btn in self.btns:
            btn.update()

def main():
    win = Window((800,600))
    btn = Button(win)
    win.run()

if __name__ == "__main__":
    main()