from abc import ABC, abstractmethod
from constants import MainCharacter


class Weapon(ABC):
    def __init__(self, scene, player, extra_width):
        self.extra_width = extra_width
        self.scene = scene
        self.player = player

    @abstractmethod
    def get_animation(self):
        pass

    def get_extra_width(self):
        return self.extra_width


class Pistol(Weapon):
    def get_animation(self):
        path = MainCharacter.ANIMATION_PATH + '/weapon/pistol'
        return {
            'none_left': ((path + '/walk_left_1.png', 1),),
            'none_right': ((path + '/walk_right_1.png', 1),),
            'walk_right': ((path + '/walk_right_0.png', 30), (path + '/walk_right_1.png', 30)),
            'walk_left': ((path + '/walk_left_0.png', 30), (path + '/walk_left_1.png', 30)),
            'jump_right': ((path + '/walk_right_1.png', 1),),
            'jump_left': ((path + '/walk_left_1.png', 1),),
        }
