import pygame as pg
from constants import Screen, Cell, Pixel
from models.LevelScene import LevelScene
from objects.MainCharacter import MainCharacter
from objects.Platform import Platform
from pygame.sprite import Group, GroupSingle


class Main(LevelScene):
    def init_objects(self):
        spawn_x, spawn_y = self.get_cell_pos(0, self.cell_height - 3)
        self.groups['main_character'] = GroupSingle(MainCharacter(self, spawn_x, spawn_y))
        n = self.height // Cell.HEIGHT
        m = self.width // Cell.WIDTH
        self.groups['platforms'] = Group()
        for i in range(0, m, 2):
            self.groups['platforms'].add(Platform(self, (i, self.cell_height - 1 - i // 2)))
        for i in range(m):
            self.groups['platforms'].add(Platform(self, (i, self.cell_height - 1)))
        self.groups['platforms'].add(Platform(self, (8, self.cell_height - 2)),
                                     Platform(self, (10, self.cell_height - 2)))
        self.groups['can_collide'] = Group(*self.groups['platforms'].sprites())
        self.groups['level_objects'] = Group(self.groups['main_character'].sprite, *self.groups['platforms'].sprites())
        super().init_objects()

    def render(self):
        for i in range((Screen.HEIGHT + Cell.HEIGHT - 1) // Cell.HEIGHT):
            for j in range((Screen.WIDTH + Cell.WIDTH - 1) // Cell.WIDTH):
                if (i + j) % 2 == 0:
                    pg.draw.rect(self.game.screen, (230, 230, 230),
                                 pg.Rect(j * Cell.WIDTH, i * Cell.HEIGHT, Cell.WIDTH, Cell.HEIGHT))
        '''
        for i in range((Screen.HEIGHT + Pixel.HEIGHT - 1) // Pixel.HEIGHT):
            for j in range((Screen.WIDTH + Pixel.WIDTH - 1) // Pixel.WIDTH):
                if (i + j) % 2 == 0:
                    pg.draw.rect(self.game.screen, (190, 190, 190),
                                 pg.Rect(j * Pixel.WIDTH, i * Pixel.HEIGHT, Pixel.WIDTH, Pixel.HEIGHT))
        '''
        super().render()
