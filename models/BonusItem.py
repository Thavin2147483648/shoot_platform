from abc import abstractmethod
import pygame as pg

from models.Animation import Animation
from models.LevelObject import StaticLevelObject
from constants import BonusItem as Properties
from enums import LevelObjectCellPositionX as PositionX, LevelObjectCellPositionY as PositionY


class BonusItem(StaticLevelObject):
    WIDTH = 0
    HEIGHT = 0
    ANIMATION = ''

    def __init__(self, scene, cell_x, cell_y, *groups, position_x=PositionX.MIDDLE, position_y=PositionY.MIDDLE):
        super().__init__(scene, cell_x, cell_y, self.WIDTH, self.HEIGHT, *groups,
                         position_x=position_x, position_y=position_y, render_level=1)
        self.animation = Animation(self, self.ANIMATION)
        self.image = pg.Surface((10, 10))

    @abstractmethod
    def on_pickup(self):
        pass

    def pickup_condition(self):
        return True

    def process_logic(self, events):
        if self.collide_with(self.scene.get_object('main_character')) and self.pickup_condition():
            self.on_pickup()
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
        self.image = self.animation.update()
