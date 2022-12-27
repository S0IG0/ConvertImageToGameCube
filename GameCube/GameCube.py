import PIL.Image
from PIL import Image, ImageDraw

BASE_CONFIGURATION = (
    'RGB',
    (9, 9),
    'black',
    'white',
)


class GameCube(object):

    @staticmethod
    def ___create_image_cube___(
            mode: b'',
            size: tuple[int, int],
            color: str,
            color_point: str,
            points: list[tuple[int, int]]) -> PIL.Image.Image:
        image = Image.new(mode, size, color)
        draw = ImageDraw.Draw(image)
        for point in points:
            draw.point(point, color_point)

        return image

    def __init__(self):
        self.sides = [
            self.___create_image_cube___(*BASE_CONFIGURATION, [(4, 4), ]),
            self.___create_image_cube___(*BASE_CONFIGURATION, [(4, 2), (4, 6), ]),
            self.___create_image_cube___(*BASE_CONFIGURATION, [(4, 2), (4, 4), (4, 6), ]),
            self.___create_image_cube___(*BASE_CONFIGURATION, [(2, 2), (2, 6), (6, 2), (6, 6), ]),
            self.___create_image_cube___(*BASE_CONFIGURATION, [(2, 2), (2, 6), (6, 2), (6, 6), (4, 4), ]),
            self.___create_image_cube___(*BASE_CONFIGURATION, [(2, 2), (2, 4), (2, 6), (6, 2), (6, 4), (6, 6)]),
        ]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self) -> PIL.Image.Image:
        if self.index < 6:
            self.index += 1
            return self.sides[self.index - 1]
        else:
            raise StopIteration


if __name__ == '__main__':
    cube = GameCube()
    for side in cube:
        side.show()
