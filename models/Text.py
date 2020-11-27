import pygame as pg

from models.GameObject import GameObject
from constants import Basic, Color, Screen


class Text(GameObject):
    def __init__(self, scene, x, y, font_size=Basic.FONT_SIZE, text='Hello, world!',
                 line_spacing=5, color=Color.ORANGE, *groups):
        super().__init__(scene, x, y, 0, 0, *groups)
        self.font = pg.font.Font(Basic.FONT_PATH, font_size)
        self.text = text
        self.color = color
        self.image = None
        self.rect = None
        self.line_spacing = line_spacing
        self.set_text(text)

    def set_text(self, text):
        self.text = text
        arr = []
        max_width = 0
        height = 0
        for i in text.split('\n'):
            image = self.font.render(i, True, self.color)
            arr.append(image)
            max_width = max(max_width, image.get_width())
            height += image.get_height()
        height += self.line_spacing * (len(arr) - 1)
        self.image = pg.Surface((max_width, height), pg.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        height = 0
        for i in arr:
            self.image.blit(i, (0, height))
            height += i.get_height() + self.line_spacing
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
