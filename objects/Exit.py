import pygame as pg

from functions import rect_collide
from models.LevelObject import LevelObject, StaticLevelObject
from constants import Exit as Properties, Cell
from enums import LevelObjectCellPositionX as PositionX, LevelObjectCellPositionY as PositionY


class Exit(StaticLevelObject):
    WIDTH = Properties.WIDTH
    HEIGHT = Properties.HEIGHT
    ANIMATION = Properties.IMAGE_PATH
    GROUP_NAME = 'exit'

    def process_logic(self, events):
        if self.collide_with(self.scene.get_object('main_character')):
            for event in events:
                if event.type == pg.KEYDOWN and event.key == pg.K_e:
                    self.scene.finish_level()
