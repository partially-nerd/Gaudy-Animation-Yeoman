# cp -r GAY $HOME/.local/lib/python3.11/site-packages; python3 Projects/quadratic_equations/
from GAY.window import Window
from GAY.maths import Graph, math
from GAY.button import Button, Slider
from GAY.shapes import Rectangle, Circle
from GAY.animate import Animate
from functools import partial as bind_function

# INITIALIZATION
animate = Animate()
window = Window(
    geometry=(800, 600),
    font="Projects/font.ttf",
    record="Projects/quadratic_equations/main_rendered",
)

graph = Graph(
    window,
    height=500,
    graph=lambda x: x**2,
    range_=(-100, 100),
    resolution=1,
    caption="y = ax²",
)

slider = Slider(window, max_value=2)


# ANIMATION METHODS
def set_slider(
    property: str = "a",
    value: float = 30,
    function: str = "x**2",
    max_value: float = None,
):
    if not (max_value is None):
        slider.max_value = max_value
    slider.set_slider(property, value)
    graph.fn = lambda x: eval(
        function.replace("$", f"({round(value, 3)})").replace("x", f"({x})")
    )


def set_caption(caption):
    def function():
        graph.caption.text = caption

    return function


def animate_graph(
    property: str = "a",
    from_: float = 30,
    to: float = 100,
    function: str = "x**2",
    max_value: float = None,
    timing_fn=animate.ease_in_out,
):
    def animation(t):
        set_slider(
            property,
            animate.lerp(from_, to, timing_fn(t)),
            function,
            max_value,
        )

    return animation


window.play(
    [animate_graph("a", -2, 2, "$*x**2", timing_fn=animate.haste_in_out), -1],
    duration=4,
)
window.play(
    animate_graph("a", -2, 1, "$*x**2", timing_fn=animate.haste_in_out), duration=4
)
window.play(animate.delay_one_second)
window.play(
    animate_graph("c", 0, 20, "x**2+$", 20),
    animate.do_once(set_caption("y = x² + c")),
    duration=4,
)
window.play([animate_graph("c", -20, 20, "x**2+$", 20), -1], duration=4)
window.play(animate_graph("c", -20, 20, "x**2+$", 20), duration=4)
window.play([animate_graph("c", 0, 20, "x**2+$", 20), -1], duration=4)
window.play(animate.delay_one_second)
window.play(
    animate_graph("b", 0, 20, "x**2+x*$", 20),
    animate.do_once(set_caption("y = x² + bx")),
    duration=4,
)
window.play([animate_graph("b", -20, 20, "x**2+x*$", 20), -1], duration=4)
window.play(animate_graph("b", -20, 0, "x**2+x*$", 20), duration=4)
window.play(animate.delay_one_second)
window.play(animate.do_once(window.quit))

window.run()
