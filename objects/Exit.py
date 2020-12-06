import pygame as pg

from functions import rect_collide
from models.LevelObject import LevelObject, StaticLevelObject
from constants import Exit as Properties, Cell
from enums import LevelObjectCellPositionX as PositionX, LevelObjectCellPositionY as PositionY


class Exit(StaticLevelObject):
    def __init__(self, scene, cell_x, cell_y, *groups, width=Properties.WIDTH, height=Properties.HEIGHT):
        super().__init__(scene, cell_x, cell_y, width, height, *groups,
                         position_x=PositionX.LEFT, position_y=PositionY.BOTTOM)
        self.image = pg.image.load(Properties.IMAGE_PATH)
        self.rect = self.get_render_rect()

    def process_logic(self, events):
        if self.collide_with(self.scene.get_object('main_character')):
            for event in events:
                if event.type == pg.KEYDOWN and event.key == pg.K_e:
                    self.scene.finish_level()
            
    def update(self, *args, **kwargs):
        if self.collide_with(self.scene.get_object('main_character')):
            self.scene.get_object('to_exit_text').show()
        else:
            self.scene.get_object('to_exit_text').hide()
        super().update(*args, **kwargs)
