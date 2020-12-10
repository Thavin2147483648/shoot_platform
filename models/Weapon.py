from abc import ABC, abstractmethod
from constants import MainCharacter, Bullet as BulletProperties
from enums import DirectionX
from functions import is_intersection
from models.Float import Float
from objects.Bullet import Bullet


class Weapon(ABC):
    OFFSET_Y = 0
    RELOAD_TIME = 0
    CAPACITY = 0
    EXTRA_WIDTH = 0

    def __init__(self, scene, player):
        self.scene = scene
        self.player = player
        self.remaining = self.CAPACITY
        self.remaining_time = 0
        self.last_frames = 0

    @abstractmethod
    def get_animation(self):
        pass

    @abstractmethod
    def fire(self):
        pass

    @abstractmethod
    def can_fire(self):
        pass

    def get_extra_width(self):
        return self.EXTRA_WIDTH


class Pistol(Weapon):
    OFFSET_Y = 42
    RELOAD_TIME = 40
    CAPACITY = 8
    EXTRA_WIDTH = 24

    def get_animation(self):
        path = MainCharacter.ANIMATION_PATH + '/weapon/pistol'
        dct = {
            'none_left': ((path + '/walk_left_1.png', 1),),
            'none_right': ((path + '/walk_right_1.png', 1),),
            'walk_right': ((path + '/walk_right_0.png', 30), (path + '/walk_right_1.png', 30)),
            'walk_left': ((path + '/walk_left_0.png', 30), (path + '/walk_left_1.png', 30)),
            'jump_right': ((path + '/walk_right_1.png', 1),),
            'jump_left': ((path + '/walk_left_1.png', 1),),
        }
        delay = (1, 1, 5, 5)
        for d in ('left', 'right'):
            name = 'shoot_' + d
            dct[name] = []
            for i in range(4):
                dct[name].append((path + '/shooting/' + d + '_' + str(i) + '.png', delay[i]))
            dct[name] = tuple(dct.get(name))
        return dct

    def fire(self):
        if not self.can_fire():
            return False
        d = self.player.get_last_x_direction()
        d_str = ('left' if d == DirectionX.LEFT else 'right')
        if d == DirectionX.LEFT:
            bullet = Bullet(self.scene, self.player.get_x1() - self.get_extra_width() - BulletProperties.WIDTH,
                            self.player.get_y1() + self.OFFSET_Y, d)
        else:
            bullet = Bullet(self.scene, self.player.get_x2() + self.get_extra_width(),
                            self.player.get_y1() + self.OFFSET_Y, d)
        self.scene.groups['main'].add(bullet)
        self.scene.groups['can_collide'].add(bullet)
        self.set_remaining(self.remaining - 1)
        self.remaining_time = self.RELOAD_TIME
        self.player.animation.play_once('shoot_' + d_str)
        self.last_frames = self.scene.game.get_frames()

    def get_remaining(self):
        return self.remaining

    def reload(self):
        self.set_remaining(self.CAPACITY)

    def set_remaining(self, value):
        self.remaining = sorted([0, value, self.CAPACITY])[1]
        self.scene.get_object('ammo_indicator').set_current(self.remaining)

    def update_remaining_time(self):
        t = self.scene.game.get_frames() - self.last_frames
        self.last_frames = self.scene.game.get_frames()
        self.remaining_time = max(0, self.remaining_time - t)

    def can_fire(self):
        if self.remaining == 0:
            return False
        self.update_remaining_time()
        if self.remaining_time > 0:
            return False
        d = self.player.get_last_x_direction()
        if d == DirectionX.LEFT:
            rect = (self.player.get_x1() - self.get_extra_width() - BulletProperties.WIDTH, self.player.get_y1(),
                    self.player.get_x1(), self.player.get_y2())
        else:
            rect = (self.player.get_x2(), self.player.get_y1(),
                    self.player.get_x2() + self.get_extra_width() + BulletProperties.WIDTH, self.player.get_y2())
        if Float(rect[0]) < 0 or Float(rect[2]) > self.scene.get_width() or \
                Float(rect[1]) < 0 or Float(rect[3]) > self.scene.get_height():
            return False
        for obj in self.scene.get_objects('can_collide'):
            if is_intersection(rect, obj.get_rect()):
                return False
        return True
