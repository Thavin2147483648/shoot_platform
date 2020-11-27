import pygame as pg

from abc import ABC, abstractmethod
from pygame.sprite import Sprite, AbstractGroup
from models.Scene import Scene


class GameObject(Sprite):
    def __init__(self, scene: Scene, x, y, width, height, *groups: AbstractGroup):
        self.scene = scene
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        super().__init__(*groups)

    def get_rect(self):
        return pg.Rect(self.x, self.y, self.width, self.height)

    @abstractmethod
    def process_logic(self, events):
        pass
