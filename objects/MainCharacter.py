import pygame as pg
from math import sqrt

from enums import DirectionX
from models.Animation import Animation
from models.Float import Float
from models.LevelObject import LevelObject
from constants import MainCharacter as Properties, Color, Screen, Gravitation, Cell
from functions import custom_round
from models.Weapon import Pistol


class MainCharacter(LevelObject):
    def __init__(self, scene, spawn_cell: tuple, *groups, width=Properties.WIDTH, height=Properties.HEIGHT):
        super().__init__(scene, Cell.WIDTH * spawn_cell[0] + (Cell.WIDTH - width) // 2,
                         Cell.HEIGHT * (spawn_cell[1] + 1) - height, width, height, *groups)
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.speed_y = Float(0)
        self.speed_x = Float(0)
        self.last_x_direction = DirectionX.LEFT
        self.animation = Animation(self, Properties.ANIMATION, 'none')
        self.weapon = None
        self.set_weapon(Pistol(self.scene, self, 24))
        self.image = self.animation.get_current_image()

    def is_grounded(self):
        if Float(self.speed_y) != 0:
            return False
        for obj in self.scene.get_objects('can_collide'):
            if self.get_x2() > obj.get_x1() and self.get_x1() < obj.get_x2() and self.get_y2() == obj.get_y1():
                return True
        return False

    def get_weapon_extra_width(self):
        if self.weapon is None:
            return 0
        return self.weapon.extra_width

    def set_weapon(self, weapon):
        self.weapon = weapon
        self.animation.override_animations(weapon.get_animation())

    def add_vectors(self, vector_x, vector_y):
        # Oy
        if Float(self.get_y() + vector_y) < 0:
            vector_y = max(vector_y, -self.get_y())
            self.speed_y = 0
        for obj in self.scene.get_objects('can_collide'):
            if self.get_x2() > obj.get_x1() and self.get_x1() < obj.get_x2():
                if self.get_y2() <= obj.get_y1() < Float(self.get_y2() + vector_y):
                    vector_y = obj.get_y1() - self.get_y2()
                    self.speed_y = 0
                if self.get_y1() >= obj.get_y2() > Float(self.get_y1() + vector_y):
                    vector_y = obj.get_y2() - self.get_y1()
                    self.speed_y = 0
        self.y += vector_y
        # Ox
        if Float(self.get_x1() + vector_x) < 0 or Float(self.get_x2() + vector_x) > Float(self.scene.get_width()):
            vector_x = sorted([-self.get_x1(), vector_x, Float(self.scene.get_width() - self.get_x2())])[1]
            self.speed_x = 0
        for obj in self.scene.get_objects('can_collide'):
            if self.get_y2() > obj.get_y1() and self.get_y1() < obj.get_y2():
                if self.get_x2() <= obj.get_x1() < Float(self.get_x2() + vector_x):
                    vector_x = obj.get_x1() - self.get_x2()
                    self.speed_x = 0
                if self.get_x1() >= obj.get_x2() > Float(self.get_x1() + vector_x):
                    vector_x = obj.get_x2() - self.get_x1()
                    self.speed_x = 0
        self.x += vector_x

    def update_camera_rect(self):
        super(MainCharacter, self).update_camera_rect()
        if self.last_x_direction == DirectionX.LEFT:
            self.rect.x -= self.get_weapon_extra_width()

    def update_sprite(self):
        self.rect = self.get_render_rect()
        self.image = self.animation.update()

    def process_logic(self, events):
        pressed = pg.key.get_pressed()
        if pressed[pg.K_a]:
            self.speed_x = -Properties.X_SPEED
        if pressed[pg.K_d]:
            self.speed_x = Properties.X_SPEED
        if pressed[pg.K_SPACE]:
            if self.is_grounded():
                self.speed_y = -sqrt(2 * Gravitation.G * Properties.JUMP_HEIGHT)
        if not self.is_grounded():
            self.speed_y += Gravitation.G
        vector_x = Float(self.speed_x)
        vector_y = Float(self.speed_y)
        self.add_vectors(vector_x, vector_y)
        self.speed_x = Float(self.speed_x)
        self.speed_y = Float(self.speed_y)
        if self.get_y() >= self.scene.height:
            self.scene.game_over()
        if self.speed_x != 0:
            print('CHECK 2')
            self.last_x_direction = (DirectionX.RIGHT if self.speed_x > 0 else DirectionX.LEFT)
        d = ('left' if self.last_x_direction == DirectionX.LEFT else 'right')
        if self.speed_x != 0:
            if self.speed_x > 0:
                if self.is_grounded():
                    self.animation.set_animation('walk_right')
                else:
                    self.animation.set_animation('jump_right')
            else:
                if self.is_grounded():
                    self.animation.set_animation('walk_left')
                else:
                    self.animation.set_animation('jump_left')
        else:
            self.animation.set_animation('none_' + d)
        self.speed_x = 0
        self.update_sprite()
