class Animate:
    def __init__(self) -> None:
        self.lerp = lambda A, B, f_T: A + (B - A) * f_T
        self.ease_in = lambda T: T**2
        self.ease_out = lambda T: 1 - (1 - T) ** 2
        self.ease_in_out = lambda T: self.lerp(self.ease_in(T), self.ease_out(T), T)

    def delay_one_second(self, t):
        return

    def do_once(self, function):
        def animation(t):
            if t != 0: return
            function()
        return animation

    def move_to_x(self, object, x):
        default_x = object.x

        def animation(t):
            object.x = self.lerp(default_x, x, self.ease_in_out(t))

        return animation

    def move_to_y(self, object, y):
        default_y = object.y

        def animation(t):
            object.y = self.lerp(default_y, y, self.ease_in_out(t))

        return animation

    def move_to(self, object, vector: tuple):
        default_x, default_y = object.x, object.y
        x, y = vector

        if default_x > x:
            default_x, x = x, default_x
        if default_y > y:
            default_y, y = y, default_y

        def animation(t):
            object.x = self.lerp(default_x, x, self.ease_in_out(t))
            object.y = self.lerp(default_y, y, self.ease_in_out(t))

        return animation

    def fade_out(self, object):
        def animation(t):
            object.alpha = self.lerp(0, 255, self.ease_in_out(t))
            if t <= 0:
                object.visible = False

        return animation

    def fade_in(self, object):
        def animation(t):
            if t != 0:
                object.alpha = self.lerp(0, 255, self.ease_in_out(t))
            else:
                object.visible = True

        return animation
