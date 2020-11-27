class Basic:
    NAME = 'ShootPlatform'
    FRAME_DELAY = 20
    FONT_PATH = 'fonts/pixel_font.ttf'
    FONT_SIZE = 40


class Screen:
    WIDTH = 960
    HEIGHT = 800


class Pixel:
    WIDTH = 4
    HEIGHT = 4


class Cell:
    WIDTH = 80
    HEIGHT = 80


class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    ORANGE = (255, 92, 0)


class MainCharacter:
    WIDTH = 48
    HEIGHT = 96
    JUMP_HEIGHT = 3 * Cell.HEIGHT + 30
    X_SPEED = 8
    IMAGE_PATH = 'textures/animations/main_character/none.png'


class Gravitation:
    G = 1


class Platform:
    WIDTH = Cell.WIDTH
    HEIGHT = Cell.HEIGHT // 2
    IMAGE_PATH = 'textures/ground.png'


class Coin:
    WIDTH = 32
    HEIGHT = 32
    IMAGE_PATH = 'textures/coin.png'
    SCORE_ADD = 100
    HESITATION_S = tuple(
        [0] * 1 + [1] * 1 + [2] * 1 + [3] * 1 + [4] * 1 + [5] * 2 + [6] * 2
    )
