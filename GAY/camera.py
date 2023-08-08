class Camera:
    def __init__(self, position: tuple = (0, 0, 1000)) -> None:
        self.x, self.y, self.z = position

    def project(self, object: tuple[int]):
        x, y, z = object
        x_projected, y_projected = (self.z * (self.x + x)) / (self.z + z), (
            self.z * (self.y + y)
        ) / (self.z + z)
        return x_projected, y_projected
