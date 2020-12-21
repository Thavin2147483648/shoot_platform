from abc import ABC
import json
from os import path

from models.BarIndicator import BarIndicator
from models.LevelObject import LevelObject
from models.Scene import Scene
from models.Camera import Camera
from constants import Cell, Screen
from pygame.sprite import Group, GroupSingle

from objects.AmmoIndicator import AmmoIndicator
from objects.Block import Block
from objects.CircleDetector import CircleDetector
from objects.Exit import Exit
from objects.HealthIndicator import HealthIndicator
from objects.Platform import Platform
from objects.Player import Player
from objects.PlayerSpawn import PlayerSpawn
from objects.Score import Score
from objects.ToExitText import ToExitText
from objects.bonus_items.Ammo import Ammo
from objects.bonus_items.Coin import Coin
from objects.Air import Air
from objects.Wall import Wall
from models.Text import TextAlign, PositionalText, PositionX, PositionY
from objects.enemies.Turret import Turret


class LevelScene(Scene, ABC):
    OBJ_CLASSES = {
        'coin': Coin,
        'ammo': Ammo,
        'exit': Exit,
        'platform': Platform,
        'wall': Wall,
        'block': Block,
        'turret': Turret
    }

    """
    camera_obj_name - имя объекта, за которым следит камера
    """

    def __init__(self, game, index, level_id=1, camera_obj_name='player'):
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

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def init_objects(self):
        self.groups['can_collide'] = Group()
        self.groups['damageable'] = Group()
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
            self.add_object(obj)
            self.T[spawn_cell[0]][spawn_cell[1]] = obj
            for obj_name in data['objects'].keys():
                for obj_data in data['objects'][obj_name]:
                    pos = int(obj_data['x']), int(obj_data['y'])
                    obj = self.OBJ_CLASSES[obj_name](self, *pos)
                    self.add_object(obj)
                    self.T[pos[0]][pos[1]] = obj
        self.add_object(AmmoIndicator(self))
        self.add_object(HealthIndicator(self))
        self.add_objects(Player(self, self.get_object('player_spawn').get_cell_pos()),
                         Score(self), ToExitText(self))
        obj = self.get_object(self.camera_obj)
        self.camera = Camera(obj, inner_size=(obj.width * 3, obj.height * 2))

    def add_object(self, obj):
        super(LevelScene, self).add_object(obj)
        if isinstance(obj, LevelObject):
            if obj.can_collide:
                self.groups['can_collide'].add(obj)
            if obj.damageable:
                self.groups['damageable'].add(obj)

    def add_objects(self, *objects):
        for obj in objects:
            self.add_object(obj)

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
        super().render()
