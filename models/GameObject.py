import pygame as pg

from abc import ABC, abstractmethod
from pygame.sprite import Sprite, AbstractGroup

from models.Animation import Animation
from models.Scene import Scene
from functions import is_intersection, get_surface
from models.Float import Float
from enums import PositionX, PositionY
from constants import Screen


class GameObject(Sprite):
    WIDTH = 0
    HEIGHT = 0
    ANIMATION = get_surface(10, 10)

    def __init__(self, scene: Scene, x: float, y: float,
                 *groups: AbstractGroup, render_level=0):
        self.scene = scene
        self.x = x
        self.y = y
        self.width = int(self.WIDTH)
        self.height = int(self.HEIGHT)
        self.render_level = render_level
        if type(self.ANIMATION) is not Animation:
            self.animation = Animation(self, self.ANIMATION)
        else:
            self.animation = self.ANIMATION
        super().__init__(*groups)

    def get_render_rect(self):
        return pg.Rect(int(Float(self.x)), int(Float(self.y)), self.width, self.height)

    def get_render_image(self):
        return self.animation.get_current_image()

    def set_image(self, image):
        self.animation.override_animation('none', image)

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
        self.animation.update()
        self.image = self.get_render_image()
        super().update(*args, **kwargs)

    def process_logic(self, events):
        pass


class PositionalGameObject(GameObject):
    def __init__(self, scene, position_x: PositionX, position_y: PositionY, *groups,
                 offset=(10, 10), render_level=3):
        super().__init__(scene, 0, 0, *groups, render_level=render_level)
        self.position_x = position_x
        self.position_y = position_y
        self.offset = offset
        self.update_position()

    def update_position(self):
        if self.position_x == PositionX.LEFT:
            self.x = self.offset[0]
        elif self.position_x == PositionX.MIDDLE:
            self.x = (Screen.WIDTH - self.width) // 2
        elif self.position_x == PositionX.RIGHT:
            self.x = Screen.WIDTH - self.width - self.offset[0]
        # Oy
        if self.position_y == PositionY.TOP:
            self.y = self.offset[1]
        elif self.position_y == PositionY.MIDDLE:
            self.y = (Screen.HEIGHT - self.height) // 2
        elif self.position_y == PositionY.BOTTOM:
            self.y = Screen.HEIGHT - self.height - self.offset[1]
        self.x = Float(self.x)
        self.y = Float(self.y)
        self.rect = self.get_render_rect()

    def process_logic(self, events):
        pass
