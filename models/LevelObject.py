import pygame as pg
from pygame.sprite import AbstractGroup

from models import LevelScene
from models.GameObject import GameObject
from functions import is_intersection, rect_collide
from enums import LevelObjectCellPositionX as PositionX, LevelObjectCellPositionY as PositionY
from constants import Cell


class LevelObject(GameObject):
    CAN_COLLIDE = False

    def __init__(self, scene: LevelScene, x, y, *groups: AbstractGroup, render_level=2):
        super().__init__(scene, x, y, *groups, render_level=render_level)
        self.can_collide = self.CAN_COLLIDE

    def get_render_rect(self):
        camera = self.scene.get_camera()
        rect = super(LevelObject, self).get_render_rect()
        rect.x -= camera.x
        rect.y -= camera.y
        return rect

    def update(self, *args, **kwargs) -> None:
        super().update(*args, **kwargs)
        camera = self.scene.get_camera()
        if not camera.can_see(self):
            self.hide()
        else:
            self.show()


class StaticLevelObject(LevelObject):
    CELL_POSITION_X = PositionX.MIDDLE
    CELL_POSITION_Y = PositionY.BOTTOM

    def __init__(self, scene, cell_x, cell_y, *groups, render_level=1):
        super().__init__(scene, 0, 0, *groups, render_level=render_level)
        self.cell_x = cell_x
        self.cell_y = cell_y
        self.position_x = self.CELL_POSITION_X
        self.position_y = self.CELL_POSITION_Y
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

    def get_cell_pos(self):
        return self.cell_x, self.cell_y
