import pygame as pg

from abc import ABC, abstractmethod
from pygame.sprite import Sprite, AbstractGroup
from models.Scene import Scene
from functions import is_intersection
from models.Float import Float


class GameObject(Sprite):
    def __init__(self, scene: Scene, x: float, y: float, width: int, height: int, *groups: AbstractGroup, render_level=0):
        self.scene = scene
        self.x = x
        self.y = y
        self.width = int(width)
        self.height = int(height)
        self.render_level = render_level
        super().__init__(*groups)

    def get_render_rect(self):
        return pg.Rect(int(Float(self.x)), int(Float(self.y)), self.width, self.height)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_x(self):
        return Float(self.x)

    def get_x1(self):
        return self.get_x()

    def get_x2(self):
        return Float(self.x + self.width)

    def get_y(self):
        return Float(self.y)

    def get_y1(self):
        return self.get_y()

    def get_y2(self):
        return Float(self.y + self.height)

    def get_rect(self):
        return self.get_x1(), self.get_y1(), self.get_x2(), self.get_y2()

    def show(self):
        self.add(self.scene.to_render[self.render_level])

    def hide(self):
        self.remove(self.scene.to_render[self.render_level])

    def collide_with(self, obj):
        return is_intersection(self.get_rect(), obj.get_rect())

    def update(self, *args, **kwargs) -> None:
        self.rect = self.get_render_rect()
        super().update(*args, **kwargs)

    @abstractmethod
    def process_logic(self, events):
        pass
