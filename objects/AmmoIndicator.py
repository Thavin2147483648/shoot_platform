from enums import PositionX, PositionY
from constants import AmmoIndicator as Properties
from models.GameObject import PositionalGameObject
import pygame as pg


class AmmoIndicator(PositionalGameObject):
    def __init__(self, scene, *groups, position_x=PositionX.LEFT, position_y=PositionY.BOTTOM):
        super().__init__(scene, position_x, position_y, 0, 0, *groups)
        self.max = 0
        self.current = 0
        self.full_image = pg.image.load(Properties.FULL_IMAGE_PATH)
        self.empty_image = pg.image.load(Properties.EMPTY_IMAGE_PATH)
        self.set_current(self.max)

    def attach_weapon(self, weapon=None):
        if weapon is None:
            self.max = 0
            self.current = 0
            self.width = 0
            self.height = 0
        else:
            self.max = weapon.CAPACITY
            self.width = Properties.WIDTH * self.max + Properties.OFFSET_X * (self.max - 1)
            self.height = Properties.HEIGHT
            self.set_current(weapon.get_remaining())

    def update_surface(self):
        self.image = pg.Surface((self.width, self.height), pg.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        for i in range(self.max):
            if i < self.current:
                img = self.full_image
            else:
                img = self.empty_image
            self.image.blit(img, ((Properties.WIDTH + Properties.OFFSET_X) * i, 0))
        self.update_position()

    def set_current(self, value):
        if 0 <= value <= self.max:
            self.current = value
            self.update_surface()

    def process_logic(self, events):
        pass
