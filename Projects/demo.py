# python3 demo.py
from GAY.window import Window
from GAY.button import Button
from GAY.shapes import Rectangle, Circle
from GAY.maths import Graph, math
from GAY.shapes import line
from GAY.animate import Animate
from functools import partial as bind_function

# INITIALIZATION
animate = Animate()
window = Window(
    geometry=(800, 600),
    font="Projects/font.otf",
    record="Projects/demo",
)

rect = Rectangle(window)
circle = Circle(window, (200, 200), visible=False)
graph = Graph(window, height=500, resolution=0.1, graph=lambda x: 0)


# ANIMATION METHODS
def animate_rotating_slope(t):
    graph.fn = (
        lambda x: math.tan(
            animate.lerp(
                0,
                math.pi / 2,
                animate.ease_in_out(t),
            )
        )
        * x**2
    )


def change_equation():
    graph.fn = lambda x: x


window.animation_list = [
    [[animate_rotating_slope, -1]],
    [[animate.delay_one_second]],
    [
        [animate.fade_in(circle)],
        [animate.fade_out(rect), -1],
        [animate.fade_out(graph), -1],
    ],
    [
        [animate.move_to_x(circle, 0)],
        [animate.move_to_y(circle, 0)],
    ],
    [
        [animate.do_once(change_equation)],
        [animate.fade_in(graph)],
    ],
]

window.run()
