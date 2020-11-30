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
from objects.PlayerSpawn import PlayerSpawn
from objects.Score import Score
from objects.Coin import Coin
from objects.Air import Air
from models.Text import TextAlign, PositionalText, TextPositionX, TextPositionY


class LevelScene(Scene, ABC):
    OBJ_CLASSES = {
        'coin': Coin,
        'exit': Exit,
        'platform': Platform
    }

    """
    camera_obj_name - имя объекта, за которым следит камера
    """
    def __init__(self, game, index, level_id=1, camera_obj_name='main_character'):
        self.camera = None
        self.cell_width = 0
        self.cell_height = 0
        self.id = level_id
        self.file_path = f'levels_data/{level_id}.json'
        self.width = self.cell_width * Cell.WIDTH
        self.height = self.cell_height * Cell.HEIGHT
        self.camera = None
        self.camera_obj = camera_obj_name
        self.T = None
        super().__init__(game, index)

    def init_objects(self):
        for obj in self.OBJ_CLASSES.keys():
            self.groups[obj] = Group()
        self.groups['player_spawn'] = GroupSingle()
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            self.cell_width = data['width']
            self.cell_height = data['height']
            self.T = []
            for i in range(self.cell_width):
                self.T.append([])
                for j in range(self.cell_height):
                    self.T[i].append(Air(self, i, j))
            self.width = self.cell_width * Cell.WIDTH
            self.height = self.cell_height * Cell.HEIGHT
            spawn_cell = int(data['spawn']['x']), int(data['spawn']['y'])
            obj = PlayerSpawn(self, *spawn_cell)
            self.groups['player_spawn'].add(obj)
            self.T[spawn_cell[0]][spawn_cell[1]] = obj
            for obj_name in data['objects'].keys():
                for obj_data in data['objects'][obj_name]:
                    pos = int(obj_data['x']), int(obj_data['y'])
                    obj = self.OBJ_CLASSES[obj_name](self, *pos)
                    self.groups[obj_name].add(obj)
                    self.T[pos[0]][pos[1]] = obj
        self.groups['can_collide'] = Group(*self.get_objects('platform'))
        self.groups['main_character'] = GroupSingle(MainCharacter(self,
                                                                  (self.get_object('player_spawn').cell_x,
                                                                   self.get_object('player_spawn').cell_y)))
        self.groups['score'] = GroupSingle(Score(self))
        self.groups['level_objects'] = Group(self.get_object('main_character'), self.get_object('player_spawn'))
        for i in self.OBJ_CLASSES.keys():
            self.groups['level_objects'].add(*self.get_objects(i))
        self.groups['to_exit_text'] = GroupSingle(PositionalText(self, TextPositionX.RIGHT,
                                                                 TextPositionY.TOP,
                                                                 text="Press E\nto exit level",
                                                                 align=TextAlign.RIGHT, offset=(10, 10)))
        obj = self.get_object(self.camera_obj)
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
                level_data = data.get(str(self.id), {})
                return level_data.get('max_score', 0)
        return 0

    def update_stats(self):
        data = self.get_all_stats()
        score = self.get_object('score').get()
        level_data = data.get(str(self.id), {})
        level_data['max_score'] = max(level_data.get('max_score', 0), score)
        data[str(self.id)] = level_data
        with open('level_stats.json', 'w') as file:
            json.dump(data, file)

    def render(self):
        self.camera.update()
        self.groups['level_objects'].update()
        super().render()
