from models.Float import Float
from models.LevelObject import LevelObject
from constants import Bullet as Properties
import pygame as pg
from enums import DirectionX


class Bullet(LevelObject):
    WIDTH = Properties.WIDTH
    HEIGHT = Properties.HEIGHT

    def __init__(self, scene, x, y, direction_x, *groups):
        super().__init__(scene, x, y, *groups)
        self.set_image(Properties.LEFT_IMAGE_PATH if direction_x == DirectionX.LEFT
                       else Properties.RIGHT_IMAGE_PATH)
        self.speed_x = Properties.SPEED
        if direction_x == DirectionX.LEFT:
            self.speed_x *= -1

    def add_vector_x(self, vector):
        if Float(self.get_x1() + vector) < 0 or Float(self.get_x2() + vector) > Float(self.scene.get_width()):
            vector = sorted([-self.get_x1(), vector, Float(self.scene.get_width() - self.get_x2())])[1]
            self.speed_x = 0
        for obj in self.scene.get_objects('can_collide'):
            if self.get_y2() > obj.get_y1() and self.get_y1() < obj.get_y2():
                if self.get_x2() <= obj.get_x1() < Float(self.get_x2() + vector):
                    vector = obj.get_x1() - self.get_x2()
                    self.speed_x = 0
                if self.get_x1() >= obj.get_x2() > Float(self.get_x1() + vector):
                    vector = obj.get_x2() - self.get_x1()
                    self.speed_x = 0
        self.x += vector

    def process_logic(self, events):
        if Float(self.speed_x) == 0:
            self.kill()
        else:
            vector_x = self.speed_x
            self.add_vector_x(vector_x)
