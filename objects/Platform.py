import pygame as pg
from constants import Color
from models.GameObject import GameObject


class Platform(GameObject):
    def __init__(self, scene, index, name, pos, size):
        super().__init__(scene, index, name)
        self.width = size[0]
        self.height = size[1]
        self.x = pos[0]
        self.y = pos[1]

    def process_logic(self, events):
        pass

    def render(self, screen):
        pg.draw.rect(screen, Color.BLACK, pg.Rect(self.x, self.y, self.width, self.height))
