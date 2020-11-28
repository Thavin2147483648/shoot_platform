import pygame as pg
from constants import Screen, Cell, Pixel
from models.LevelScene import LevelScene
from objects.MainCharacter import MainCharacter
from objects.Platform import Platform
from pygame.sprite import Group, GroupSingle


class Main(LevelScene):
    def __init__(self, game, index, add_cell_grid=True, add_pixel_grid=False):
        super().__init__(game, index)
        self.grid = pg.Surface((Screen.WIDTH, Screen.HEIGHT), pg.SRCALPHA)
        self.grid.fill((0, 0, 0, 0))
        if add_cell_grid:
            for i in range((Screen.HEIGHT + Cell.HEIGHT - 1) // Cell.HEIGHT):
                for j in range((Screen.WIDTH + Cell.WIDTH - 1) // Cell.WIDTH):
                    if (i + j) % 2 == 0:
                        pg.draw.rect(self.grid, (230, 230, 230),
                                     pg.Rect(j * Cell.WIDTH, i * Cell.HEIGHT, Cell.WIDTH, Cell.HEIGHT))
        if add_pixel_grid:
            for i in range((Screen.HEIGHT + Pixel.HEIGHT - 1) // Pixel.HEIGHT):
                for j in range((Screen.WIDTH + Pixel.WIDTH - 1) // Pixel.WIDTH):
                    if (i + j) % 2 == 0:
                        pg.draw.rect(self.grid, (200, 200, 200), pg.Rect(j * Pixel.WIDTH, i * Pixel.HEIGHT,
                                                                         Pixel.WIDTH, Pixel.HEIGHT))

    def render(self):
        self.game.screen.blit(self.grid, (0, 0))
        super().render()
