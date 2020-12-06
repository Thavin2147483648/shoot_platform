import pygame as pg

from functions import rect_collide
from models.LevelObject import LevelObject, StaticLevelObject
from constants import Coin as Properties, Cell
from enums import LevelObjectCellPositionX as PositionX, LevelObjectCellPositionY as PositionY


class Coin(StaticLevelObject):
    def __init__(self, scene, cell_x, cell_y, *groups, width=Properties.WIDTH, height=Properties.HEIGHT,
                 render_level=1):
        super().__init__(scene, cell_x, cell_y, width, height, *groups,
                         position_x=PositionX.MIDDLE, position_y=PositionY.MIDDLE, render_level=render_level)
        self.image = pg.image.load(Properties.IMAGE_PATH)
        self.rect = self.get_render_rect()

    def process_logic(self, events):
        if self.collide_with(self.scene.get_object('main_character')):
            self.scene.get_object('score').add(Properties.SCORE_ADD)
            self.kill()
        frames = self.scene.game.get_frames() % (4 * len(Properties.HESITATION_S))
        s_ind = frames % (2 * len(Properties.HESITATION_S))
        if s_ind >= len(Properties.HESITATION_S):
            s = Properties.HESITATION_S[2 * len(Properties.HESITATION_S) - s_ind - 1]
        else:
            s = Properties.HESITATION_S[s_ind]
        if frames >= 2 * len(Properties.HESITATION_S):
            s *= -1
        self.y = self.get_coords()[1] + s
