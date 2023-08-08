# python3 demo.py
from GAY.window import Window
from GAY.camera import Camera
from GAY.wireframes import Pyramid
from GAY.animate import Animate
from functools import partial as bind_function

# INITIALIZATION
animate = Animate()
window = Window(geometry=(800, 600))
camera = Camera()
pyramid  = Pyramid(window, camera)

def animate_camera_x(t):
    camera.x = animate.lerp(0, 200, animate.ease_in_out(t))

def animate_camera_y(t):
    camera.y = animate.lerp(0, 200, animate.ease_in_out(t))

# ANIMATION METHODS
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