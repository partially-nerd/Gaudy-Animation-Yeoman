# python3 demo.py
from GAY.window import Window
from GAY.button import Button
from GAY.shapes import Rectangle, Circle
from GAY.animate import Animate
from functools import partial as func


def main():
    animate = Animate()
    win = Window(geometry=(800, 600))
    btn = Button(win)
    circ = Circle(win, position=(250, 0))
    rect = Rectangle(win, position=(100, 200))

    def animate_rect_y(T):
        rect.y = animate.lerp(0, 200, animate.ease_in_out(T))

    def animate_rect_x(T):
        rect.x = animate.lerp(100, 150, animate.ease_in_out(T))

    def animate_circ_r(T):
        circ.r = animate.lerp(25, 50, animate.ease_in_out(T))

    def btn_onclick(self):
        win.animation_list = [
            [
                [
                    animate_rect_y,
                    "-",
                ],
                [
                    animate_rect_x,
                    "+",
                ],
            ],
            [[animate_circ_r, "+"]],
        ]

    btn.onclick = func(btn_onclick, btn)

    win.run()


if __name__ == "__main__":
    main()
