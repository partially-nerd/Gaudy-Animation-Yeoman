from pygame.draw import line
from numpy import array
from operator import add


class Wireframe:
    def __init__(
        self,
        canvas,
        camera,
        vertex_table: list,
        edge_map: list[tuple],
        outline_color: str = "#6290a6",
        line_width: int = 2,
    ) -> None:
        self.canvas = canvas
        self.color = outline_color
        self.line_width = line_width
        self.canvas.elements.append(self)
        self.camera = camera
        self.vertices = vertex_table
        self.edges = edge_map

    def update(self):
        self.projected_vertices = []
        for vertex in self.vertices:
            self.projected_vertices.append(self.camera.project(vertex))
        for edges in self.edges:
            line(
                self.canvas.canvas,
                self.color,
                self.projected_vertices[edges[0]],
                self.projected_vertices[edges[1]],
                self.line_width,
            )


class Cube(Wireframe):
    def __init__(
        self,
        canvas,
        camera,
        side_length: int = 100,
        position: tuple[int] = (100, 100, 0),
    ) -> None:
        self.side_length = side_length
        self.x, self.y, self.z = position
        super().__init__(
            canvas,
            camera,
            array(
                [
                    [
                        self.side_length * x,
                        self.side_length * y,
                        self.side_length * z,
                    ]
                    for x, y, z in [
                        [0, 0, 1],
                        [1, 0, 1],
                        [1, 0, 0],
                        [0, 0, 0],
                        [0, 1, 1],
                        [1, 1, 1],
                        [1, 1, 0],
                        [0, 1, 0],
                    ]
                ]
            )
            + array(
                [
                    [self.x, self.y, self.z],
                    [self.x, self.y, self.z],
                    [self.x, self.y, self.z],
                    [self.x, self.y, self.z],
                    [self.x, self.y, self.z],
                    [self.x, self.y, self.z],
                    [self.x, self.y, self.z],
                    [self.x, self.y, self.z],
                ]
            ),
            [
                (0, 1),
                (1, 2),
                (2, 3),
                (3, 0),
                (4, 5),
                (5, 6),
                (6, 7),
                (4, 7),
                (0, 4),
                (1, 5),
                (2, 6),
                (3, 7),
            ],
        )


class Pyramid(Wireframe):
    def __init__(
        self,
        canvas,
        camera,
        side_length: int = 100,
        height: int = 200,
        position: tuple[int] = (100, 100, 0),
    ) -> None:
        self.side_length = side_length
        self.height = height
        self.x, self.y, self.z = position
        super().__init__(
            canvas,
            camera,
            array(
                [
                    [0 * self.side_length, 1 * self.side_length, 2 * self.side_length],
                    [0 * self.side_length, 1 * self.side_length, 0 * self.side_length],
                    [2 * self.side_length, 1 * self.side_length, 0 * self.side_length],
                    [2 * self.side_length, 1 * self.side_length, 2 * self.side_length],
                    [1 * self.side_length, 2 * -self.height, 1 * self.side_length],
                ]
            ) / 2
            + array(
                [
                    [self.x, self.y + self.height, self.z],
                    [self.x, self.y + self.height, self.z],
                    [self.x, self.y + self.height, self.z],
                    [self.x, self.y + self.height, self.z],
                    [self.x, self.y + self.height, self.z],
                ]
            ),
            [
                (0, 1),
                (1, 2),
                (2, 3),
                (3, 0),
                (0, 4),
                (1, 4),
                (2, 4),
                (3, 4),
            ],
        )
