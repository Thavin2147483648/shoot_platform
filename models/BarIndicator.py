from math import ceil

import pygame as pg
from functions import get_surface
from models.Float import Float
from models.GameObject import GameObject


class BarIndicatorColor:
    def __init__(self, background, border, full, empty):
        self.background = background
        self.border = border
        self.full = full
        self.empty = empty


class BarIndicator:
    def __init__(self, width: int, height: int, color: BarIndicatorColor = None,
                 border_size: tuple = (4, 4), max_value=100, current=0):
        self.width = width
        self.height = height
        if color is None:
            color = BarIndicatorColor((10, 10, 10), (100, 100, 100), (255, 0, 0), (0, 0, 0))
        self.color = color
        self.max = max_value
        self.border_size = border_size
        self.current = 0
        self.image = get_surface(self.width, self.height)
        self.set_current(current)

    def update_image(self):
        image = get_surface(self.width, self.height)
        image.fill(self.color.border)
        offset_x, offset_y = self.border_size
        image.fill(self.color.background, (offset_x, offset_y, self.width - 2 * offset_x, self.height - 2 * offset_y))
        cnt = self.width - 2 * offset_x
        cnt = int(Float(ceil(cnt * self.current / self.max)))
        image.fill(self.color.full, (offset_x, offset_y, cnt, self.height - 2 * offset_y))
        self.image = image

    def get_image(self, update=False):
        if update:
            self.update_image()
        return self.image

    def set_current(self, value):
        if 0 <= value <= self.max:
            self.current = value
            self.update_image()
