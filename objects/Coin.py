import pygame as pg

from functions import rect_collide
from models.LevelObject import LevelObject
from constants import Coin as Properties, Cell


class Coin(LevelObject):
    def __init__(self, scene, spawn_cell, width=Properties.WIDTH, height=Properties.HEIGHT, *groups):
        self.spawn = (spawn_cell[0] * Cell.WIDTH + (Cell.WIDTH - width) // 2,
                      spawn_cell[1] * Cell.HEIGHT + (Cell.HEIGHT - height) // 2)
        super().__init__(scene, *self.spawn, width, height, *groups)
        self.image = pg.image.load(Properties.IMAGE_PATH)
        self.rect = self.get_rect()

    def process_logic(self, events):
        if rect_collide(self.scene.groups['main_character'].sprite.get_rect(), self.get_rect()):
            self.scene.groups['score'].sprite.add(Properties.SCORE_ADD)
            self.kill()
        frames = self.scene.game.get_frames() % (4 * len(Properties.HESITATION_S))
        s_ind = frames % (2 * len(Properties.HESITATION_S))
        s = None
        if s_ind >= len(Properties.HESITATION_S):
            s = Properties.HESITATION_S[2 * len(Properties.HESITATION_S) - s_ind - 1]
        else:
            s = Properties.HESITATION_S[s_ind]
        if frames >= 2 * len(Properties.HESITATION_S):
            s *= -1
        self.y = self.spawn[1] + s
