class Basic:
    NAME = 'ShootPlatform'
    FRAME_DELAY = 20


class Screen:
    WIDTH = 960
    HEIGHT = 800


class Cell:
    WIDTH = 80
    HEIGHT = 80


class Pixel:
    WIDTH = 4
    HEIGHT = 4


class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)


class MainCharacter:
    WIDTH = 48
    HEIGHT = 96
    LYING_WIDTH = 96
    LYING_HEIGHT = 48
    JUMP_HEIGHT = 3 * Cell.HEIGHT + 30
    X_SPEED = 8
    LYING_SPEED = 4
    IMAGE_PATH = 'textures/animations/main_character/none.png'


class Gravitation:
    G = 1


class Platform:
    WIDTH = Cell.WIDTH
    HEIGHT = Cell.HEIGHT
    IMAGE_PATH = 'textures/ground.png'
