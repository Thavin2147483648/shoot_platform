import pygame as pg
from constants import Screen, Player, Color
from functions import rect_collide, is_intersection
from models.Float import Float


class Camera:
    def __init__(self, obj, outer_size=(Screen.WIDTH, Screen.HEIGHT), inner_size=None):
        self.x = 0.0
        self.y = 0.0
        self.outer_size = outer_size
        if inner_size is None:
            inner_size = (obj.width, obj.height)
        if inner_size[0] < min(outer_size[0], obj.width) or inner_size[1] < min(outer_size[1], obj.height):
            exit(-1)
        self.inner_size = inner_size
        self.obj = obj
        self.width = self.outer_size[0]
        self.height = self.outer_size[1]
        self.inner_offset = ((self.outer_size[0] - self.inner_size[0]) // 2,
                             (self.outer_size[1] - self.inner_size[1]) // 2)

    def get_inner_pos(self):
        return self.x + self.inner_offset[0], self.y + self.inner_offset[1]

    def get_rect(self):
        return Float(self.x), Float(self.y), Float(self.x + self.width), Float(self.y + self.height)

    def draw_border(self, screen):
        pos1 = self.inner_offset
        pos2 = (pos1[0] + self.inner_size[0], pos1[1] + self.inner_size[1])
        pg.draw.line(screen, Color.RED, pos1, (pos2[0], pos1[1]))
        pg.draw.line(screen, Color.RED, pos1, (pos1[0], pos2[1]))
        pg.draw.line(screen, Color.RED, pos2, (pos1[0], pos2[1]))
        pg.draw.line(screen, Color.RED, pos2, (pos2[0], pos1[1]))

    def can_see(self, obj):
        return is_intersection((0, 0, self.width, self.height), obj.get_render_rect())

    def update(self):
        inner_pos = self.get_inner_pos()
        if Float(inner_pos[0]) > Float(self.obj.get_x()):
            self.x -= inner_pos[0] - self.obj.get_x()
        elif Float(self.obj.get_x2()) > Float(inner_pos[0] + self.inner_size[0]):
            self.x += self.obj.get_x2() - (inner_pos[0] + self.inner_size[0])
        if Float(inner_pos[1]) > Float(self.obj.get_y()):
            self.y -= inner_pos[1] - self.obj.get_y()
        elif Float(self.obj.get_y2()) > Float(inner_pos[1] + self.inner_size[1]):
            self.y += self.obj.get_y2() - (inner_pos[1] + self.inner_size[1])
        self.x = sorted([0, self.x, self.obj.scene.width - self.width])[1]
        self.y = sorted([0, self.y, self.obj.scene.height - self.height])[1]
