from map_reduce import map_reduce
from Matrix import Matrix
from PIL import Image


def generate_matrix(image: Image.Image) -> Matrix:
    matrix = []

    width, height = image.size
    pixels = image.load()

    for i in range(width):
        matrix.append([])
        for j in range(height):
            r, g, b = pixels[i, j]
            matrix[i].append(int(map_reduce(((r + g + b) // 3), 0, 255, 0, 6)))

    return Matrix(matrix)


if __name__ == '__main__':
    print(generate_matrix(Image.open(r'../data/test.png'), ).matrix[0])
