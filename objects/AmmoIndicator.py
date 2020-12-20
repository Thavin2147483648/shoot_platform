from enums import PositionX, PositionY
from constants import AmmoIndicator as Properties
from functions import get_surface
from models.GameObject import PositionalGameObject
import pygame as pg


class AmmoIndicator(PositionalGameObject):
    GROUP_NAME = 'ammo_indicator'

    def __init__(self, scene, *groups, position_x=PositionX.RIGHT, position_y=PositionY.BOTTOM):
        super().__init__(scene, position_x, position_y, *groups)
        self.max = 0
        self.current = 0
        self.full_image = pg.image.load(Properties.FULL_IMAGE_PATH)
        self.empty_image = pg.image.load(Properties.EMPTY_IMAGE_PATH)
        self.column_count = 0
        self.row_count = 0
        self.set_current(self.max)

    def attach_weapon(self, weapon):
        self.max = weapon.CAPACITY
        self.column_count = weapon.AMMO_INDICATOR_COLUMN_SIZE
        self.row_count = (self.max + self.column_count - 1) // self.column_count
        self.width = Properties.WIDTH * min(self.max, self.column_count)
        self.width += Properties.OFFSET_X * (min(self.max, self.column_count) - 1) * int(self.max != 0)
        self.height = Properties.HEIGHT * self.row_count
        self.height += Properties.OFFSET_Y * (self.row_count - 1) * int(self.max != 0)
        self.set_current(weapon.get_remaining())

    def update_surface(self):
        image = get_surface(self.width, self.height)
        for i in range(self.max):
            if i < self.current:
                img = self.full_image
            else:
                img = self.empty_image
            x = (Properties.WIDTH + Properties.OFFSET_X) * (i % self.column_count)
            y = (Properties.HEIGHT + Properties.OFFSET_Y) * (i // self.column_count)
            image.blit(img, (x, y))
        self.set_image(image)
        self.update_position()

    def set_current(self, value):
        if 0 <= value <= self.max:
            self.current = value
            self.update_surface()
