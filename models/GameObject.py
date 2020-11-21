from abc import ABC, abstractmethod


class GameObject(ABC):
    def __init__(self, scene, index, name):
        self.scene = scene
        self.index = index
        self.name = name

    @abstractmethod
    def process_logic(self, events):
        pass

    @abstractmethod
    def render(self, screen):
        pass
