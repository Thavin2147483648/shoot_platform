import pygame as pg
from enums import TextAlign, PositionX, PositionY

from models.GameObject import GameObject, PositionalGameObject
from constants import Basic, Color


class Text(GameObject):
    def __init__(self, scene, *groups, x=0, y=0, font_size=Basic.FONT_SIZE, text='Hello, world!',
                 line_spacing=5, align=TextAlign.LEFT, color=Color.ORANGE, render_level=3):
        super().__init__(scene, x, y, 0, 0, *groups, render_level=render_level)
        self.font = pg.font.Font(Basic.FONT_PATH, font_size)
        self.text = text
        self.color = color
        self.line_spacing = line_spacing
        self.align = align
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
            x = 0
            if self.align == TextAlign.LEFT:
                x = 0
            elif self.align == TextAlign.CENTER:
                x = (max_width - i.get_width()) // 2
            elif self.align == TextAlign.RIGHT:
                x = max_width - i.get_width()
            self.image.blit(i, (x, height))
            height += i.get_height() + self.line_spacing
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pg.Rect((self.x, self.y), self.image.get_size())

    def process_logic(self, events):
        pass


class PositionalText(Text, PositionalGameObject):
    def __init__(self, scene, position_x: PositionX, position_y: PositionY, *groups,
                 font_size=Basic.FONT_SIZE, line_spacing=5, align=TextAlign.LEFT, color=Color.ORANGE,
                 text='Hello, world!', offset=(10, 10)):
        super().__init__(scene, *groups, font_size=font_size, line_spacing=line_spacing,
                         align=align, color=color, text=text)
        self.position_x = position_x
        self.position_y = position_y
        self.offset = offset
        self.update_position()

    def set_text(self, text):
        super().set_text(text)
        self.update_position()
