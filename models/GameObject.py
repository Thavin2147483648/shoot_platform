from abc import ABC, abstractmethod
from pygame.sprite import Sprite, AbstractGroup
from models.Scene import Scene


class GameObject(Sprite):
    def __init__(self, scene: Scene, *groups: AbstractGroup):
        super().__init__(*groups)
        self.scene = scene

    @abstractmethod
    def process_logic(self, events):
        pass
