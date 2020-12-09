from abc import abstractmethod
import pygame as pg

from models.Animation import Animation
from models.LevelObject import StaticLevelObject
from constants import BonusItem as Properties
from enums import LevelObjectCellPositionX as PositionX, LevelObjectCellPositionY as PositionY


class BonusItem(StaticLevelObject):
    CELL_POSITION_X = PositionX.MIDDLE
    CELL_POSITION_Y = PositionY.MIDDLE

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
