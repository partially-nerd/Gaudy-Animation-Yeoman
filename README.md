# Gaudy Animation Yeoman
Gaudy Animation Yeoman (GAY for short) is an animation engine made with pygame, that includes features like click-detection, lerp, etc.

- _New: Now has recording support (record parameter when initializing Window object)_
- _New: Now has alpha support_
- _New: New widgets - Graph, Sliders_
- _New: Now has new timing functions - hasteIn, hasteOut, hasteInOut_
- _New: Now has vscode snippets_

# Demo

https://github.com/partially-nerd/Gaudy-Animation-Yeoman/assets/108736691/e7923c38-2369-4b58-9cb1-4c61a8378be3

_Generated from the main:/Projects/quadratic_equations file_

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

win.play([animate_rect_y, -1], animate_rect_x) # Since the y-value is decreasing, we pass a list of [fn, direction], where direction = -1
win.play(animate_circle_r)

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

window.play(animate_camera_x)
window.play(animate_camera_y)

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

window.play(animate_rotating_slope)

window.run()
```
