import pygame as pg
from models.LevelObject import StaticLevelObject
from constants import Wall as Properties
from enums import LevelObjectCellPositionX as PositionX, LevelObjectCellPositionY as PositionY


class Wall(StaticLevelObject):
    def __init__(self, scene, cell_x, cell_y, *groups, width=Properties.WIDTH, height=Properties.HEIGHT,
                 position_x=PositionX.MIDDLE, position_y=PositionY.BOTTOM, render_level=1):
        super().__init__(scene, cell_x, cell_y, width, height, *groups, position_x=position_x, position_y=position_y,
                         render_level=render_level)
        self.image = pg.image.load(Properties.IMAGE_PATH)
        self.rect = self.get_render_rect()
