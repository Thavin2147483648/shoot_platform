import pygame as pg
from constants import Screen, Cell, Pixel
from models.LevelScene import LevelScene
from objects.MainCharacter import MainCharacter
from objects.Platform import Platform
from pygame.sprite import Group, GroupSingle


class Main(LevelScene):
    def render(self):
        for i in range((Screen.HEIGHT + Cell.HEIGHT - 1) // Cell.HEIGHT):
            for j in range((Screen.WIDTH + Cell.WIDTH - 1) // Cell.WIDTH):
                if (i + j) % 2 == 0:
                    pg.draw.rect(self.game.screen, (230, 230, 230),
                                 pg.Rect(j * Cell.WIDTH, i * Cell.HEIGHT, Cell.WIDTH, Cell.HEIGHT))
        super().render()
