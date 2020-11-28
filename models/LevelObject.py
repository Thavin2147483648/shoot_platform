import pygame as pg
from pygame.sprite import AbstractGroup

from models import LevelScene
from models.GameObject import GameObject
from functions import is_intersection
from enums import LevelObjectCellPositionX as PositionX, LevelObjectCellPositionY as PositionY
from constants import Cell


class LevelObject(GameObject):
    def __init__(self, scene: LevelScene, x, y, width, height, *groups: AbstractGroup):
        super().__init__(scene, x, y, width, height, *groups)

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


class StaticLevelObject(LevelObject):
    def __init__(self, scene, cell_x, cell_y, width, height, *groups, position_x=PositionX.MIDDLE,
                 position_y=PositionY.BOTTOM):
        super().__init__(scene, 0, 0, width, height, *groups)
        self.cell_x = cell_x
        self.cell_y = cell_y
        self.position_x = position_x
        self.position_y = position_y
        self.x, self.y = self.get_coords()

    def get_coords(self):
        x = self.cell_x * Cell.WIDTH
        if self.position_x == PositionX.MIDDLE:
            x += (Cell.WIDTH - self.width) // 2
        elif self.position_x == PositionX.RIGHT:
            x += Cell.WIDTH - self.width
        y = self.cell_y * Cell.HEIGHT
        if self.position_y == PositionY.MIDDLE:
            y += (Cell.HEIGHT - self.height) // 2
        elif self.position_y == PositionY.BOTTOM:
            y += Cell.HEIGHT - self.height
        return x, y
