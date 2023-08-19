from pygame import init as initialize_pygame, quit, QUIT, MOUSEBUTTONDOWN
from pygame.display import set_mode, flip
from pygame.image import save
from pygame.time import Clock
from pygame.freetype import Font
from pygame.mouse import get_pos
from pygame.event import get as get_events
import ffmpeg
from shutil import rmtree
from os import mkdir


class Window:
    t_negative = 1
    t_positive = 0
    running: bool = True
    fps: int = 60
    btns: list = []
    animation_list = []
    elements: list = []

    def __init__(
        self, geometry: tuple[int], font, background_color: str = "#1a1a1a", record=None
    ) -> None:
        initialize_pygame()
        self.w, self.h = geometry
        self.font = Font(file=font, size=20)
        self.canvas = set_mode(geometry)
        self.clock = Clock()
        self.background_color = background_color
        self.record = record

    def run(self):
        if self.record is not None:
            mkdir(f"{self.record}.out")
            self.t = 0
        while self.running:
            for event in get_events():
                if event.type == QUIT:
                    self.running = False
                    if self.record is not None:
                        ffmpeg.input(
                            f"{self.record}.out/*.jpeg",
                            pattern_type="glob",
                            framerate=self.fps,
                        ).output(f"{self.record}.mp4").run()
                        rmtree(f"{self.record}.out")
                        quit()
                elif event.type == MOUSEBUTTONDOWN:
                    mouse = get_pos()
                    for btn in self.btns:
                        btn.check_click(mouse)
            self.canvas.fill(self.background_color)
            self.animate()
            self.update()
            flip()
            self.clock.tick(self.fps)
            if self.record is not None:
                save(self.canvas, f"{self.record}.out/{str(self.t).rjust(5, '0')}.jpeg")
                self.t += 1
        quit()

    def animate(self):
        if self.animation_list.__len__() == 0:
            return
        direction = None
        for animation in self.animation_list[0]:
            try:
                function, direction = animation
            except:
                function = animation[0]
                direction = 1
            if direction == 1:
                if self.t_positive >= 1:
                    self.t_positive = 0
                    self.t_negative = 1
                    self.animation_list.pop(0)
                    return
                function(self.t_positive)
            elif direction == -1:
                if self.t_negative <= 0:
                    self.t_negative = 1
                    self.t_positive = 0
                    self.animation_list.pop(0)
                    return
                function(self.t_negative)
        self.t_negative -= 1 / self.fps
        self.t_positive += 1 / self.fps

    def update(self):
        for item in self.elements:
            item.update()
