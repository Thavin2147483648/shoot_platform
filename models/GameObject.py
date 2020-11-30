import pygame as pg

from abc import ABC, abstractmethod
from pygame.sprite import Sprite, AbstractGroup
from models.Scene import Scene
from functions import rect_collide


class GameObject(Sprite):
    def __init__(self, scene: Scene, x, y, width, height, *groups: AbstractGroup, render_level=0):
        self.scene = scene
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.render_level = render_level
        super().__init__(*groups)

    def get_rect(self):
        return pg.Rect(self.x, self.y, self.width, self.height)

    def show(self):
        self.add(self.scene.to_render[self.render_level])

    def hide(self):
        self.remove(self.scene.to_render[self.render_level])

    def collide_with(self, obj):
        return rect_collide(self.get_rect(), obj.get_rect())

    @abstractmethod
    def process_logic(self, events):
        pass
