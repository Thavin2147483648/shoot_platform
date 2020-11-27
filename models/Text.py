import pygame as pg

from models.GameObject import GameObject
from constants import Basic, Color, Screen


class Text(GameObject):
    def __init__(self, scene, x, y, font_size=Basic.FONT_SIZE, text='Hello, world!', color=Color.ORANGE, *groups):
        super().__init__(scene, x, y, 0, 0, *groups)
        self.font = pg.font.Font(Basic.FONT_PATH, font_size)
        self.text = text
        self.color = color
        self.image = None
        self.rect = None
        self.set_text(text)

    def set_text(self, text):
        self.text = text
        self.image = self.font.render(self.text, True, self.color)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        # WORKAROUND
        x = self.x
        if x < 0:
            x += Screen.WIDTH
            x = x - self.width + 1
        self.rect = pg.Rect((x, self.y), self.image.get_size())

    def process_logic(self, events):
        pass
