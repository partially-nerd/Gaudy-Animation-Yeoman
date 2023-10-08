# Gaudy Animation Yeoman
Gaudy Animation Yeoman (GAY for short) is an animation engine made with pygame, that includes features like click-detection, lerp, etc.

- _New: Now has recording support (record parameter when initializing Window object)_
- _New: Now has alpha support_
- _New: New widgets - Graph, Sliders_
- _New: Now has new timing functions - hasteIn, hasteOut, hasteInOut_
- _New: Now has vscode snippets_

# Demo


https://github.com/partially-nerd/Gaudy-Animation-Yeoman/assets/108736691/770c48cf-44f9-4479-9267-4d9d5f5b183f


## Code for Demo
```py
from GAY.window import Window
from GAY.maths import Graph, math
from GAY.button import Button, Slider
from GAY.shapes import Rectangle, Circle
from GAY.animate import Animate
from functools import partial as bind_function

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
from GAY.window import Window
from GAY.maths import Graph, math
from GAY.button import Button, Slider
from GAY.shapes import Rectangle, Circle
from GAY.animate import Animate
from functools import partial as bind_function

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
```

# Documentation
## Installation
The library works locally on windows machines too, but for easy global installation on gnu/linux or bsd machines, run `cp -r GAY $HOME/.local/lib/python3.11/site-packages`

#### Dependencies
- Python3
- pygame
- ffmpeg-python

_demo.py should clear everything up_

## Boilerplate
```py
from GAY.window import Window
from GAY.animate import Animate
{{ Other Imports}}
from functools import partial as assign_function

window = Window(geometry=(400, 400))
animate = Animate()

{{Your Code}}

window.run()
```

## Examples
### Rectangle
```py
from GAY.window import Window
from GAY.animate import Animate
from GAY.shapes import Rectangle
from functools import partial as assign_function

window = Window(geometry = (400, 400))
animate = Animate()
rect = Rectangle(
    window,
    position = (100, 100),
    geometry = (200, 100),
    background_color = "#eb5e54"
)
window.run()
```

### Button
```py
from GAY.window import Window
from GAY.animate import Animate
from GAY.button import Button
from functools import partial as assign_function

window = Window(geometry = (400, 400))
animate = Animate()
btn = Button(
    window,
    text = "Hello!",
    position = (100, 100),
    geometry = (200, 100)
)

def on_click(self):
    print("Hello, World!")

btn.onclick = assign_function(on_click, btn)

window.run()
```

### Animation
```py
from GAY.window import Window
from GAY.animate import Animate
from GAY.shapes import Circle, Rectangle
from functools import partial as assign_function

animate = Animate()
win = Window(geometry=(800, 600))
circ = Circle(win, position=(250, 0))
rect = Rectangle(win, position=(100, 200))

def animate_rect_y(T):
    rect.y = animate.lerp(0, 200, animate.ease_in_out(T))

def animate_rect_x(T):
    rect.x = animate.lerp(100, 150, animate.ease_in_out(T))

def animate_circ_r(T):
    circ.r = animate.lerp(25, 50, animate.ease_in_out(T))

win.animation_list = [
    [
        [
            animate_rect_y,
            "-", # Since the y-value is decreasing
        ],
        [
            animate_rect_x,
            "+", # Since the x-value is increasing
        ],
        # These two will run simultaneously, ie. x, and y will change at the same time
    ],
    [[animate_circ_r, "+"]] # After the previous animation is completed, then the circle's radius is animated
]

win.run()
```

### 3D Animations [NEW]

```py
from GAY.window import Window
from GAY.camera import Camera
from GAY.wireframes import Pyramid
from GAY.animate import Animate
from functools import partial as bind_function

animate = Animate()
window = Window(geometry=(800, 600))
camera = Camera()
pyramid  = Pyramid(window, camera)

def animate_camera_x(t):
    camera.x = animate.lerp(0, 200, animate.ease_in_out(t))

def animate_camera_y(t):
    camera.y = animate.lerp(0, 200, animate.ease_in_out(t))

window.animation_list = [
    [
        [
            animate_camera_x,
            "+"
        ],
    ],
    [
        [
            animate_camera_y,
            "+"
        ],
    ]
]

window.run()
```

### Graph [NEW]
```py
from GAY.window import Window
from GAY.button import Button
from GAY.shapes import Rectangle, Circle
from GAY.maths import Graph, math
from GAY.animate import Animate
from functools import partial as bind_function

animate = Animate()
window = Window(geometry=(800, 600))
graph = Graph(window, resolution=0.1, graph=lambda x: 0)

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
```
