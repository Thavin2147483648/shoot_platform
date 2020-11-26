import pygame as pg
from pygame.sprite import AbstractGroup

from models.GameObject import GameObject
from functions import is_intersection


class LevelObject(GameObject):
    def __init__(self, scene, x, y, width, height, *groups: AbstractGroup):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        super().__init__(scene, *groups)

    def update_camera_rect(self):
        camera = self.scene.get_camera()
        self.rect.x = self.x - camera.x
        self.rect.y = self.y - camera.y

    def update(self, *args, **kwargs) -> None:
        camera = self.scene.get_camera()
        self.update_camera_rect()
        if not is_intersection(
                (self.rect.x, self.rect.y, self.rect.x + self.rect.width - 1, self.rect.y + self.rect.height - 1),
                (0, 0, camera.width - 1, camera.height - 1)):
            self.remove(self.scene.groups['to_render'])
        else:
            self.add(self.scene.groups['to_render'])
            super().update(args, kwargs)

    def get_rect(self):
        return pg.Rect(self.x, self.y, self.width, self.height)

    def process_logic(self, events):
        pass
