from GameCube.GameCube import GameCube
from ImageFilter.ImageFilter import generate_matrix
from PIL import Image


def main():
    cube = GameCube()
    matrix = generate_matrix(Image.open(r'data/test3.png'), 5)
    width, height = [i * j for i, j in zip(list(cube)[0].size, matrix.size)]
    width_cube, height_cube = list(cube)[0].size

    image = Image.new('RGB', (width, height), 'white')

    sides = list(cube)

    for index_line, line in enumerate(matrix.matrix):
        index_line *= width_cube
        for index_digit, digit in enumerate(line):
            index_digit *= height_cube
            image.paste(sides[digit], (index_line, index_digit))

    image.save(r'out/out.png')
    image.show()


if __name__ == '__main__':
    main()
