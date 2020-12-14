from models.LevelObject import StaticLevelObject
from constants import Block as Properties


class Block(StaticLevelObject):
    WIDTH = Properties.WIDTH
    HEIGHT = Properties.HEIGHT
    ANIMATION = Properties.IMAGE_PATH
    CAN_COLLIDE = True
    GROUP_NAME = 'block'
