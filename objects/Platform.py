import pygame as pg
from constants import Color, Cell, Platform as Properties
from models.GameObject import GameObject
from functions import custom_round
from models.LevelObject import StaticLevelObject
from enums import LevelObjectCellPositionX as PositionX, LevelObjectCellPositionY as PositionY


class Platform(StaticLevelObject):
    WIDTH = Properties.WIDTH
    HEIGHT = Properties.HEIGHT
    ANIMATION = Properties.IMAGE_PATH
    CELL_POSITION_X = PositionX.MIDDLE
    CELL_POSITION_Y = PositionY.TOP
    CAN_COLLIDE = True
