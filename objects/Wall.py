import pygame as pg
from models.LevelObject import StaticLevelObject
from constants import Wall as Properties
from enums import LevelObjectCellPositionX as PositionX, LevelObjectCellPositionY as PositionY


class Wall(StaticLevelObject):
    WIDTH = Properties.WIDTH
    HEIGHT = Properties.HEIGHT
    ANIMATION = Properties.IMAGE_PATH
    CAN_COLLIDE = True
