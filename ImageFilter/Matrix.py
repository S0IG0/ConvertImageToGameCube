from dataclasses import dataclass, field


@dataclass
class Matrix(object):
    matrix: list[list[object | int]]
    size = [0, 0]

    def __post_init__(self):
        self.size[0], self.size[1] = len(self.matrix), len(self.matrix[0])


if __name__ == '__main__':
    matrix = Matrix([[1, 1, 1, 1], [1, 1, 1, 1]])
    print(matrix.size)
