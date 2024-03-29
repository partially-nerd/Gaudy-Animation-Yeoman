from numpy import sin, cos, array


class Camera:
    def __init__(self, canvas, position: tuple = (0, 0, 400)) -> None:
        self.x, self.y, self.z = position
        self.canvas = canvas

    def rotation_x(self, theta):
        return array(
            [[1, 0, 0], [0, cos(theta), -sin(theta)], [0, sin(theta), cos(theta)]]
        )

    def rotation_y(self, theta):
        return array(
            [[cos(theta), 0, sin(theta)], [0, 1, 0], [-sin(theta), 0, cos(theta)]]
        )

    def rotation_z(self, theta):
        return array(
            [
                [cos(theta), -sin(theta), 0],
                [sin(theta), cos(theta), 0],
                [0, 0, 1],
            ]
        )

    def project(self, object: tuple[int]):
        x, y, z = object
        x_projected, y_projected = (self.z * (self.x + x)) / (self.z + z), (
            self.z * (self.y + y)
        ) / (self.z + z)
        return (self.canvas.w + x_projected) / 2, (self.canvas.h + y_projected) / 2
