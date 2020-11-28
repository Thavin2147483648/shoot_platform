from abc import ABC
import pygame as pg
import json
from os import path

from models.Scene import Scene
from models.Camera import Camera
from constants import Cell, Color
from pygame.sprite import Group, GroupSingle

from objects.Exit import Exit
from objects.Platform import Platform
from objects.MainCharacter import MainCharacter
from objects.Score import Score
from objects.Coin import Coin
from models.Text import Text, TextAlign, PositionalText, TextPositionX, TextPositionY


class LevelScene(Scene, ABC):
    """
    camera_obj_name - имя объекта, за которым следит камера
    """

    def __init__(self, game, index, level_id=1, camera_obj_name='main_character'):
        self.camera = None
        self.cell_width = 0
        self.cell_height = 0
        self.spawn_cell = (0, 0)
        self.id = level_id
        self.file_path = f'levels_data/{level_id}.json'
        print(self.file_path)
        self.width = self.cell_width * Cell.WIDTH
        self.height = self.cell_height * Cell.HEIGHT
        self.camera = None
        self.camera_obj = camera_obj_name
        super().__init__(game, index)

    def init_objects(self):
        self.groups['platforms'] = Group()
        self.groups['coins'] = Group()
        self.groups['exits'] = Group()
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            self.cell_width = data['width']
            self.cell_height = data['height']
            self.width = self.cell_width * Cell.WIDTH
            self.height = self.cell_height * Cell.HEIGHT
            self.spawn_cell = (data['spawn']['x'], data['spawn']['y'])
            for p in data['platforms']:
                self.groups['platforms'].add(Platform(self, (p['x'], p['y'])))
            for c in data['coins']:
                self.groups['coins'].add(Coin(self, (c['x'], c['y'])))
            for i in data['exits']:
                self.groups['exits'].add(Exit(self, (i['x'], i['y'])))
        self.groups['can_collide'] = Group(*self.groups['platforms'].sprites())
        self.groups['main_character'] = GroupSingle(MainCharacter(self, self.spawn_cell))
        self.groups['score'] = GroupSingle(Score(self))
        self.groups['level_objects'] = Group(*self.groups['platforms'].sprites(),
                                             *self.groups['coins'].sprites(), *self.groups['exits'].sprites(),
                                             self.groups['main_character'].sprite)
        self.groups['to_exit_text'] = GroupSingle(PositionalText(self, TextPositionX.RIGHT,
                                                                 TextPositionY.TOP,
                                                                 text="Press E\nto exit level",
                                                                 align=TextAlign.RIGHT, offset=(10, 10)))
        obj = self.groups[self.camera_obj].sprite
        self.camera = Camera(obj, inner_size=(obj.width * 3, obj.height * 2))

    def get_camera(self):
        return self.camera

    def game_over(self):
        self.reload()

    def finish_level(self):
        self.update_stats()
        self.reload()

    @staticmethod
    def get_all_stats():
        if path.exists('level_stats.json'):
            with open('level_stats.json', 'r') as file:
                return json.load(file)
        return {}

    def get_max_score(self):
        if path.exists('level_stats.json'):
            with open('level_stats.json', 'r') as file:
                data = json.load(file)
                level_data = data.get(self.id, {})
                return level_data.get('max_score', 0)
        return 0

    def update_stats(self):
        data = self.get_all_stats()
        score = self.groups['score'].sprite.get()
        level_data = data.get(self.id, {})
        level_data['max_score'] = max(level_data.get('max_score', 0), score)
        data[self.id] = level_data
        with open('level_stats.json', 'w') as file:
            json.dump(data, file)

    def render(self):
        self.camera.update()
        self.groups['level_objects'].update()
        super().render()
