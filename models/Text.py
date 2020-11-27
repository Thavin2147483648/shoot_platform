import pygame as pg
from enums import TextAlign, TextPositionX, TextPositionY

from models.GameObject import GameObject
from constants import Basic, Color, Screen


class Text(GameObject):
    def __init__(self, scene, *groups, x=0, y=0, font_size=Basic.FONT_SIZE, text='Hello, world!',
                 line_spacing=5, align=TextAlign.LEFT, color=Color.ORANGE):
        super().__init__(scene, x, y, 0, 0, *groups)
        self.font = pg.font.Font(Basic.FONT_PATH, font_size)
        self.text = text
        self.color = color
        self.image = None
        self.rect = None
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


class PositionalText(Text):
    def __init__(self, scene, position_x: TextPositionX, position_y: TextPositionY, *groups,
                 font_size=Basic.FONT_SIZE, line_spacing=5, align=TextAlign.LEFT, color=Color.ORANGE,
                 text='Hello, world!', offset=(10, 10)):
        self.position_x = position_x
        self.position_y = position_y
        self.offset = offset
        super().__init__(scene, *groups, font_size=font_size, line_spacing=line_spacing,
                         align=align, color=color, text=text)

    def set_text(self, text):
        super().set_text(text)
        if self.position_x == TextPositionX.LEFT:
            self.x = self.offset[0]
        elif self.position_x == TextPositionX.MIDDLE:
            self.x = (Screen.WIDTH - self.width) // 2
        elif self.position_x == TextPositionX.RIGHT:
            self.x = Screen.WIDTH - self.width - self.offset[0]
        # Oy
        if self.position_y == TextPositionY.TOP:
            self.y = self.offset[1]
        elif self.position_y == TextPositionY.MIDDLE:
            self.y = (Screen.HEIGHT - self.height) // 2
        elif self.position_y == TextPositionY.BOTTOM:
            self.y = Screen.HEIGHT - self.height - self.offset[1]
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
