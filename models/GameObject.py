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
    GROUP_NAME = 'main'

    def __init__(self, scene: Scene, x: float, y: float,
                 *groups: AbstractGroup, render_level=0, width=None, height=None):
        self.scene = scene
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        if width is None:
            self.width = int(self.WIDTH)
        if height is None:
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

    def set_x(self, value):
        self.x = Float(value)

    def set_x1(self, value):
        self.set_x(value)

    def set_middle_x(self, value):
        self.set_x(value - self.get_width() / 2)

    def set_x2(self, value):
        self.set_x(value - self.get_width())

    def set_y(self, value):
        self.y = Float(value)

    def set_y1(self, value):
        self.set_y(value)

    def set_middle_y(self, value):
        self.set_y(value - self.get_height() / 2)

    def set_y2(self, value):
        self.set_y(value - self.get_height())

    def get_x(self):
        return Float(self.x)

    def get_x1(self):
        return self.get_x()

    def get_middle_x(self):
        return Float((self.get_x1() + self.get_x2()) / 2)

    def get_x2(self):
        return Float(self.x + self.width)

    def get_y(self):
        return Float(self.y)

    def get_y1(self):
        return self.get_y()

    def get_middle_y(self):
        return Float((self.get_y1() + self.get_y2()) / 2)

    def get_y2(self):
        return Float(self.y + self.height)

    def print_position(self):
        print('Position: X =', self.get_x(), ' Y =', self.get_y())

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
            self.set_x(self.offset[0])
        elif self.position_x == PositionX.MIDDLE:
            self.set_middle_x(Screen.WIDTH / 2)
        elif self.position_x == PositionX.RIGHT:
            self.set_x2(Screen.WIDTH - self.offset[0])
        # Oy
        if self.position_y == PositionY.TOP:
            self.set_y(self.offset[1])
        elif self.position_y == PositionY.MIDDLE:
            self.set_middle_y(Screen.HEIGHT / 2)
        elif self.position_y == PositionY.BOTTOM:
            self.set_y2(Screen.HEIGHT - self.offset[1])

    def process_logic(self, events):
        pass
