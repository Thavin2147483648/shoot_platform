from abc import ABC
import pygame as pg

from models.Scene import Scene
from models.Camera import Camera
from constants import Cell, Color
from functions import is_intersection


class LevelScene(Scene, ABC):
    """
    camera_obj_name - имя объекта, за которым следит камера
    """
    def __init__(self, game, index, cell_width, cell_height, camera_obj_name):
        self.camera = None
        self.T = [[]] * cell_width
        for i in range(cell_width):
            self.T[i] = [None] * cell_height
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.width = cell_width * Cell.WIDTH
        self.height = cell_height * Cell.HEIGHT
        self.camera = None
        self.camera_obj = camera_obj_name
        super().__init__(game, index)

    def get_cell_pos(self, cell_x, cell_y):
        return cell_x * Cell.WIDTH, cell_y * Cell.HEIGHT

    def init_objects(self):
        obj = self.groups[self.camera_obj].sprite
        self.camera = Camera(obj, inner_size=(obj.width * 3, obj.height * 2))

    def get_camera(self):
        return self.camera

    def render(self):
        self.camera.update()
        self.groups['level_objects'].update()
        super().render()
