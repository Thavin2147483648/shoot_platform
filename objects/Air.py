import pygame as pg
from models.LevelObject import StaticLevelObject
from constants import Cell


class Air(StaticLevelObject):
    def __init__(self, scene, cell_x, cell_y, *groups, width=Cell.WIDTH, height=Cell.HEIGHT):
        super().__init__(scene, cell_x, cell_y, width, height, *groups)
        self.image = pg.Surface((width, height), pg.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.rect = self.get_rect()
