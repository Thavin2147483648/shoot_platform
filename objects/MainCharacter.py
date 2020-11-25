import pygame as pg
import random
from math import sqrt

from models.Animation import Animation
from models.LevelObject import LevelObject
from models.LevelScene import LevelScene
from constants import MainCharacter as Properties, Color, Screen, Gravitation
from functions import custom_round


class MainCharacter(LevelObject):
    def __init__(self, scene: LevelScene, x=50, y=0, width=Properties.WIDTH, height=Properties.HEIGHT):
        super().__init__(scene, x, y, width, height)
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.speed_y = 0
        self.speed_x = 0
        anim_path = 'textures/animations/main_character'
        self.is_lying = False
        self.last_x_direction = 'left'
        self.animation = Animation(self, {
            'none': ((Properties.IMAGE_PATH, 1),),
            'walk_right': ((anim_path + '/walk_right_0.png', 15), (anim_path + '/walk_right_1.png', 15)),
            'walk_left': ((anim_path + '/walk_left_0.png', 15), (anim_path + '/walk_left_1.png', 15)),
            'jump_right': ((anim_path + '/walk_right_1.png', 1),),
            'jump_left': ((anim_path + '/walk_left_1.png', 1),),
            'lie_left': ((anim_path + '/lie_left_0.png', 1),),
            'lie_right': ((anim_path + '/lie_right_0.png', 1),),
        }, 'none')
        self.image = self.animation.get_current_image()

    def is_grounded(self):
        if self.speed_y < 0:
            return False
        if self.y + self.height >= self.scene.height:
            return True
        for obj in self.scene.groups['can_collide'].sprites():
            if self.x + self.width - 1 >= obj.x and self.x <= obj.x + obj.width - 1 and self.y + self.height == obj.y:
                return True
        return False

    def add_vectors(self, vector_x, vector_y):
        # Oy
        if vector_y < -self.y or vector_y > self.scene.height - self.height - self.y:
            vector_y = sorted([-self.y, vector_y, self.scene.height - self.height - self.y])[1]
            self.speed_y = 0
        for obj in self.scene.groups['can_collide'].sprites():
            if obj.x <= self.x + self.width - 1 and obj.x + obj.width - 1 >= self.x:
                if self.y + self.height - 1 < obj.y <= self.y + self.height - 1 + vector_y:
                    vector_y = obj.y - (self.y + self.height)
                    self.speed_y = 0
                if self.y > obj.y + obj.height - 1 >= self.y + vector_y:
                    vector_y = obj.y + obj.height - self.y
                    self.speed_y = 0
        self.y += vector_y
        # Ox
        if vector_x < -self.x or vector_x > self.scene.width - self.width - self.x:
            vector_x = sorted([-self.x, vector_x, self.scene.width - self.width - self.x])[1]
            self.speed_x = 0
        for obj in self.scene.groups['can_collide'].sprites():
            if obj.y <= self.y + self.height - 1 and obj.y + obj.height - 1 >= self.y:
                if self.x + self.width - 1 < obj.x <= self.x + self.width - 1 + vector_x:
                    vector_x = obj.x - (self.x + self.width)
                    self.speed_x = 0
                if self.x > obj.x + obj.width - 1 >= self.x + vector_x:
                    vector_x = obj.x + obj.width - self.x
                    self.speed_x = 0
        self.x += vector_x

    def update_sprite(self):
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.image = self.animation.update()

    def get_start_lying_position(self):
        rect = pg.Rect(0, self.y + (self.height - Properties.LYING_HEIGHT),
                       Properties.LYING_WIDTH, Properties.LYING_HEIGHT)
        if self.last_x_direction == 'right':
            rect.x = self.x
        elif self.last_x_direction == 'left':
            rect.x = self.x - (Properties.LYING_WIDTH - self.width)
        x1 = 0
        x2 = self.scene.width - 1
        for obj in self.scene.groups['can_collide'].sprites():
            if rect.y < obj.y + obj.height and rect.y + rect.height > obj.y:
                if obj.x + obj.width - 1 < self.x:
                    x1 = max(x1, obj.x + obj.width)
                if obj.x > self.x + self.width - 1:
                    x2 = min(x2, obj.x - 1)
        if not self.is_lying:
            print(x1, x2)
        if x2 - x1 + 1 < rect.width:
            return None
        if not self.is_lying:
            print(rect.x, rect.y)
        rect.x += max(0, x1 - rect.x)
        rect.x -= max(0, rect.x + rect.width - 1 - x2)
        return rect.x, rect.y

    def get_end_lying_position(self):
        rect = pg.Rect(0, self.y - (Properties.HEIGHT - self.height), Properties.WIDTH, Properties.HEIGHT)
        if self.last_x_direction == 'right':
            rect.x = self.x
        elif self.last_x_direction == 'left':
            rect.x = self.x + (self.width - Properties.WIDTH)
        return rect.x, rect.y

    def start_lying(self):
        pos = self.get_start_lying_position()
        if not self.is_lying and pos is not None:
            self.is_lying = True
            self.x, self.y = pos
            self.width, self.height = Properties.LYING_WIDTH, Properties.LYING_HEIGHT

    def end_lying(self):
        pos = self.get_end_lying_position()
        if self.is_lying and pos is not None:
            self.is_lying = False
            self.x, self.y = pos
            self.width, self.height = Properties.WIDTH, Properties.HEIGHT

    def process_logic(self, events):
        pressed = pg.key.get_pressed()
        if self.is_grounded() and pressed[pg.K_s]:
            self.start_lying()
        else:
            self.end_lying()
        if pressed[pg.K_a]:
            self.speed_x = -(Properties.LYING_SPEED if self.is_lying else Properties.X_SPEED)
            self.last_x_direction = 'left'
        if pressed[pg.K_d]:
            self.speed_x = (Properties.LYING_SPEED if self.is_lying else Properties.X_SPEED)
            self.last_x_direction = 'right'
        if pressed[pg.K_SPACE] and not self.is_lying:
            if self.is_grounded():
                self.speed_y = -sqrt(2 * Gravitation.G * Properties.JUMP_HEIGHT)
        if not self.is_grounded():
            self.end_lying()
            self.speed_y += Gravitation.G
        vector_x = custom_round(self.speed_x)
        vector_y = custom_round(self.speed_y)
        self.add_vectors(vector_x, vector_y)
        if custom_round(self.speed_x) != 0:
            self.last_x_direction = ('right' if self.speed_x > 0 else 'left')
            if self.is_grounded():
                self.animation.set_animation(('lie' if self.is_lying else 'walk') + '_' + self.last_x_direction)
            else:
                self.animation.set_animation('jump_' + self.last_x_direction)
        else:
            if self.is_lying:
                self.animation.set_animation('lie_' + self.last_x_direction)
            else:
                self.animation.set_animation('none')
        self.speed_x = 0
        self.update_sprite()
