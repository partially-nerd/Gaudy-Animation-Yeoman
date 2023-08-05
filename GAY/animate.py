class Animate:
    def __init__(self) -> None:
        self.lerp = lambda A, B, f_T: A + (B - A) * f_T
        self.ease_in = lambda T: T**2
        self.ease_out = lambda T: 1 - (1 - T) ** 2
        self.ease_in_out = lambda T: self.lerp(self.ease_in(T), self.ease_out(T), T)
