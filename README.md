# Gaudy Animation Yeoman
Gaudy Animation Yeoman (GAY for short) is an animation engine made with pygame, that includes features like click-detection, lerp, etc.
_New: Now has vscode snippets_
_New: Now has Graph support_

Example:

https://github.com/partially-nerd/Gaudy-Animation-Yeoman/assets/108736691/b29aed62-5aa6-4c9f-a86a-cb18c0e41eca

Code that generated it:
```py
# python3 demo.py
from GAY.window import Window
from GAY.button import Button
from GAY.shapes import Rectangle, Circle
from GAY.maths import Graph, math
from GAY.wireframes import Cube
from GAY.camera import Camera
from GAY.shapes import line
from GAY.animate import Animate
from functools import partial as bind_function

# INITIALIZATION
animate = Animate()
window = Window(
    geometry=(800, 600),
    font="Projects/font.otf",
    record="Projects/demo", # Outfile name
)
camera = Camera(window) # Only for 3D rendering

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
