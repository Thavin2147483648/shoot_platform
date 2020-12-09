from enums import PositionX, PositionY


class Basic:
    NAME = 'ShootPlatform'
    FRAME_DELAY = 10
    FONT_PATH = 'fonts/pixel_font.ttf'
    FONT_SIZE = 40
    RENDER_LEVELS = 4
    EPS = 0.00001


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
    X_SPEED = 4
    IMAGE_PATH = 'textures/animations/main_character/none.png'
    ANIMATION_PATH = 'textures/animations/main_character'
    ANIMATION = {
            'none_left': ((IMAGE_PATH, 1),),
            'none': ((IMAGE_PATH, 1),),
            'none_right': ((IMAGE_PATH, 1),),
            'walk_right': ((ANIMATION_PATH + '/walk_right_0.png', 30), (ANIMATION_PATH + '/walk_right_1.png', 30)),
            'walk_left': ((ANIMATION_PATH + '/walk_left_0.png', 30), (ANIMATION_PATH + '/walk_left_1.png', 30)),
            'jump_right': ((ANIMATION_PATH + '/walk_right_1.png', 1),),
            'jump_left': ((ANIMATION_PATH + '/walk_left_1.png', 1),),
        }


class Gravitation:
    G = 0.25


class Platform:
    WIDTH = Cell.WIDTH
    HEIGHT = Cell.HEIGHT // 2
    IMAGE_PATH = 'textures/ground.png'


class Wall:
    WIDTH = 56
    HEIGHT = 80
    IMAGE_PATH = 'textures/wall/wall.png'


class BonusItem:
    HESITATION_S = tuple(
        [0] * 2 + [1] * 2 + [2] * 2 + [3] * 2 + [4] * 2 + [5] * 3 + [6] * 3
    )


class Coin:
    WIDTH = 32
    HEIGHT = 32
    IMAGE_PATH = 'textures/coin.png'
    SCORE_ADD = 100


class Ammo:
    WIDTH = 48
    HEIGHT = 32
    IMAGE_PATH = 'textures/ammo.png'


class Exit:
    WIDTH = 80
    HEIGHT = 160
    IMAGE_PATH = 'textures/exit.png'


class PlayerSpawn:
    WIDTH = 80
    HEIGHT = 160
    IMAGE_PATH = 'textures/player_spawn.png'


class Score:
    POSITION_X = PositionX.LEFT
    POSITION_Y = PositionY.TOP
    OFFSET = (10, 10)
    COLOR = Color.ORANGE


class Bullet:
    WIDTH = 8
    HEIGHT = 4
    LEFT_IMAGE_PATH = 'textures/bullet/bullet_left.png'
    RIGHT_IMAGE_PATH = 'textures/bullet/bullet_right.png'
    SPEED = 16


class AmmoIndicator:
    WIDTH = 24
    HEIGHT = 48
    FULL_IMAGE_PATH = 'textures/bullet/indicator/full.png'
    EMPTY_IMAGE_PATH = 'textures/bullet/indicator/empty.png'
    OFFSET_X = 5
