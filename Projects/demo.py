# python3 demo.py
from GAY.window import Window
from GAY.button import Button
from GAY.shapes import Rectangle, Circle
from GAY.maths import Graph, math
from GAY.animate import Animate
from functools import partial as bind_function

# INITIALIZATION
animate = Animate()
window = Window(geometry=(800, 600))
graph = Graph(window, resolution=0.1, graph=lambda x: 0)


# ANIMATION METHODS
def animate_rotating_slope(t):
    graph.fn = lambda x: x * math.tan(
        animate.lerp(
            0,
            math.pi,
            animate.ease_in_out(t),
        )
    )


window.animation_list = [[[animate_rotating_slope, "+"]]]

window.run()
