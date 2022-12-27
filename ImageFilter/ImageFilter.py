from ImageFilter.map_reduce import map_reduce
from ImageFilter.Matrix import Matrix
from PIL import Image


def generate_matrix(image: Image.Image, max_out: int | float = 5) -> Matrix:
    matrix = []

    width, height = image.size
    pixels = image.load()

    for i in range(width):
        matrix.append([])
        for j in range(height):
            r, g, b = pixels[i, j]
            matrix[i].append(int(map_reduce(((r + g + b) // 3), 0, 255, 0, max_out)))

    return Matrix(matrix)


if __name__ == '__main__':
    print(generate_matrix(Image.open(r'../data/test.png'), ).matrix[0])
