import pygame as pg
from math import sqrt
from models.GameObject import GameObject
from objects.Platform import Platform
from constants import MainCharacter as Properties, Color, Screen, Gravitation
from functions import custom_round


class MainCharacter(GameObject):
    def __init__(self, scene, index, name):
        super().__init__(scene, index, name)
        self.width = Properties.WIDTH
        self.height = Properties.HEIGHT
        self.x = 50
        self.y = 0
        self.speed_y = 0
        self.speed_x = 0

    def is_grounded(self):
        if self.speed_y < 0:
            return False
        if self.y + self.height >= Screen.HEIGHT:
            return True
        for obj in self.scene.objects:
            if type(obj) is not Platform:
                continue
            if self.x + self.width - 1 >= obj.x and self.x <= obj.x + obj.width - 1 and self.y + self.height == obj.y:
                return True
        return False

    def add_vectors(self, vector_x, vector_y):
        # Oy
        if vector_y < -self.y or vector_y > Screen.HEIGHT - self.height - self.y:
            vector_y = sorted([-self.y, vector_y, Screen.HEIGHT - self.height - self.y])[1]
            self.speed_y = 0
        for obj in self.scene.objects:
            if type(obj) is not Platform:
                continue
            if obj.x <= self.x + self.width - 1 and obj.x + obj.width - 1 >= self.x:
                if self.y + self.height - 1 < obj.y <= self.y + self.height - 1 + vector_y:
                    vector_y = obj.y - (self.y + self.height)
                    self.speed_y = 0
                if self.y > obj.y + obj.height - 1 >= self.y + vector_y:
                    vector_y = obj.y + obj.height - self.y
                    self.speed_y = 0
        self.y += vector_y
        # Ox
        if vector_x < -self.x or vector_x > Screen.WIDTH - self.width - self.x:
            vector_x = sorted([-self.x, vector_x, Screen.WIDTH - self.width - self.x])[1]
            self.speed_x = 0
        for obj in self.scene.objects:
            if type(obj) is not Platform:
                continue
            if obj.y <= self.y + self.height - 1 and obj.y + obj.height - 1 >= self.y:
                if self.x + self.width - 1 < obj.x <= self.x + self.width - 1 + vector_x:
                    vector_x = obj.x - (self.x + self.width)
                    self.speed_x = 0
                if self.x > obj.x + obj.width - 1 >= self.x + vector_x:
                    vector_x = obj.x + obj.width - self.x
                    self.speed_x = 0
        self.x += vector_x

    def process_logic(self, events):
        vector_x = 0
        vector_y = 0
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
        self.speed_x = 0

    def render(self, screen):
        w = 5
        # head
        r = 0.3 * Properties.HEIGHT / 2 + 1
        pg.draw.circle(screen, Color.BLACK, (self.x + Properties.WIDTH / 2, self.y + r), r)
        # body
        pg.draw.line(screen, Color.BLACK, (self.x + Properties.WIDTH / 2, self.y + 0.3 * Properties.HEIGHT),
                     (self.x + Properties.WIDTH / 2, self.y + 0.7 * Properties.HEIGHT), w)
        # arms
        pg.draw.line(screen, Color.BLACK, (self.x + Properties.WIDTH / 2, self.y + 0.4 * Properties.HEIGHT),
                     (self.x, self.y + 0.7 * Properties.HEIGHT), w)
        pg.draw.line(screen, Color.BLACK, (self.x + Properties.WIDTH / 2, self.y + 0.4 * Properties.HEIGHT),
                     (self.x + Properties.WIDTH, self.y + 0.7 * Properties.HEIGHT), w)
        # legs
        pg.draw.line(screen, Color.BLACK, (self.x + Properties.WIDTH / 2, self.y + 0.7 * Properties.HEIGHT),
                     (self.x, self.y + Properties.HEIGHT), w)
        pg.draw.line(screen, Color.BLACK, (self.x + Properties.WIDTH / 2, self.y + 0.7 * Properties.HEIGHT),
                     (self.x + Properties.WIDTH, self.y + Properties.HEIGHT), w)
