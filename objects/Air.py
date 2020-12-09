import pygame as pg
from models.LevelObject import StaticLevelObject
from constants import Cell
from functions import get_surface


class Air(StaticLevelObject):
    WIDTH = Cell.WIDTH
    HEIGHT = Cell.HEIGHT
    ANIMATION = get_surface(WIDTH, HEIGHT)
