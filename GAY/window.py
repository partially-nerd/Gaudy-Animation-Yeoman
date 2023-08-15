from pygame import init as initialize_pygame, quit, QUIT, MOUSEBUTTONDOWN
from pygame.display import set_mode, flip
from pygame.time import Clock
from pygame.freetype import Font
from pygame.mouse import get_pos
from pygame.event import get as get_events


class Window:
    t_negative = 1
    t_positive = 0
    running: bool = True
    fps: int = 60
    btns: list = []
    animation_list = []
    elements: list = []

    def __init__(self, geometry: tuple[int], background_color: str = "#1a1a1a") -> None:
        initialize_pygame()
        self.w, self.h = geometry
        self.font = Font(file="GAY/font.otf", size=20)
        self.canvas = set_mode(geometry)
        self.clock = Clock()
        self.background_color = background_color

    def run(self):
        while self.running:
            for event in get_events():
                if event.type == QUIT:
                    self.running = False
                elif event.type == MOUSEBUTTONDOWN:
                    mouse = get_pos()
                    for btn in self.btns:
                        btn.check_click(mouse)
            self.canvas.fill(self.background_color)
            self.animate()
            self.update()
            flip()
            self.clock.tick(self.fps)
        quit()

    def animate(self):
        if self.animation_list.__len__() == 0:
            return
        for animation in self.animation_list[0]:
            function, direction = animation
            if direction == "+":
                if self.t_positive >= 0.98:
                    self.t_positive = 0
                    self.t_negative = 1
                    self.animation_list.pop(0)
                    return
                function(self.t_positive)
                self.t_positive += 1 / self.fps
            elif direction == "-":
                if self.t_negative <= 0.02:
                    self.t_negative = 1
                    self.t_positive = 0
                    self.animation_list.pop(0)
                    return
                function(self.t_negative)
                self.t_negative -= 1 / self.fps

    def update(self):
        for item in self.elements:
            item.update()
