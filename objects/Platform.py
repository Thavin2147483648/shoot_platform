import pygame as pg
from constants import Color, Cell, Platform as Properties
from models.GameObject import GameObject
from functions import custom_round


class Platform(GameObject):
    def __init__(self, scene, cell_pos, cell_w):
        super().__init__(scene)
        self.width = Properties.WIDTH
        self.height = Properties.HEIGHT
        self.x = cell_pos[0] * Cell.WIDTH
        self.y = cell_pos[1] * Cell.HEIGHT
        self.image = pg.image.load(Properties.IMAGE_PATH)
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def process_logic(self, events):
        pass

    def render(self, screen):
        pg.draw.rect(screen, Color.BLACK, pg.Rect(self.x, self.y, self.width, self.height))
