import pygame as pg
from math import sqrt

from models.Animation import Animation
from models.LevelObject import LevelObject
from constants import MainCharacter as Properties, Color, Screen, Gravitation, Cell
from functions import custom_round


class MainCharacter(LevelObject):
    def __init__(self, scene, spawn_cell: tuple, width=Properties.WIDTH, height=Properties.HEIGHT):
        super().__init__(scene, Cell.WIDTH * spawn_cell[0] + (Cell.WIDTH - width) // 2,
                         Cell.HEIGHT * (spawn_cell[1] + 1) - height, width, height)
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.speed_y = 0
        self.speed_x = 0
        anim_path = 'textures/animations/main_character'
        self.animation = Animation(self, {
            'none': ((Properties.IMAGE_PATH, 1),),
            'walk_right': ((anim_path + '/walk_right_0.png', 15), (anim_path + '/walk_right_1.png', 15)),
            'walk_left': ((anim_path + '/walk_left_0.png', 15), (anim_path + '/walk_left_1.png', 15)),
            'jump_right': ((anim_path + '/walk_right_1.png', 1),),
            'jump_left': ((anim_path + '/walk_left_1.png', 1),),
        }, 'none')
        self.image = self.animation.get_current_image()

    def is_grounded(self):
        if self.speed_y < 0:
            return False
        for obj in self.scene.groups['platforms'].sprites():
            if self.x + self.width - 1 >= obj.x and self.x <= obj.x + obj.width - 1 and self.y + self.height == obj.y:
                return True
        return False

    def add_vectors(self, vector_x, vector_y):
        # Oy
        if vector_y < -self.y:
            vector_y = max(vector_y, -self.y)
            self.speed_y = 0
        for obj in self.scene.groups['platforms'].sprites():
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
        for obj in self.scene.groups['platforms'].sprites():
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
        vector_x = custom_round(self.speed_x)
        vector_y = custom_round(self.speed_y)
        self.add_vectors(vector_x, vector_y)
        if self.y >= self.scene.height:
            self.scene.game_over()
        if custom_round(self.speed_x) != 0:
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
            self.animation.set_animation('none')
        self.speed_x = 0
        self.update_sprite()
