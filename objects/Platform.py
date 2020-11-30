import pygame as pg
from constants import Color, Cell, Platform as Properties
from models.GameObject import GameObject
from functions import custom_round
from models.LevelObject import StaticLevelObject
from enums import LevelObjectCellPositionX as PositionX, LevelObjectCellPositionY as PositionY


class Platform(StaticLevelObject):
    def __init__(self, scene, cell_x, cell_y, *groups, width=Properties.WIDTH, height=Properties.HEIGHT,
                 render_level=1):
        super().__init__(scene, cell_x, cell_y, width, height, *groups,
                         position_x=PositionX.MIDDLE, position_y=PositionY.TOP, render_level=render_level)
        self.image = pg.image.load(Properties.IMAGE_PATH)
        self.rect = self.get_rect()

    def process_logic(self, events):
        pass

    def render(self, screen):
        pg.draw.rect(screen, Color.BLACK, pg.Rect(self.x, self.y, self.width, self.height))
