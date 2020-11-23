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


class MainCharacter:
    WIDTH = 48
    HEIGHT = 96
    JUMP_HEIGHT = 3 * Cell.HEIGHT + 30
    X_SPEED = 8
    IMAGE_PATH = 'textures/main_character.png'


class Gravitation:
    G = 1


class Platform:
    WIDTH = Cell.WIDTH
    HEIGHT = Cell.HEIGHT // 2
    IMAGE_PATH = 'textures/ground.png'
