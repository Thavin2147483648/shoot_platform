import pygame as pg
from pygame.sprite import AbstractGroup

from models.GameObject import GameObject
from functions import is_intersection


class LevelObject(GameObject):
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
            self.hide()
        else:
            self.show()
            super().update(args, kwargs)

    def process_logic(self, events):
        pass
