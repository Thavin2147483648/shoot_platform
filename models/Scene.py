from abc import ABC, abstractmethod

from pygame.sprite import Group


class Scene(ABC):
    def __init__(self, game, index):
        self.game = game
        self.index = index
        self.groups = {}

    def reload(self):
        self.groups = {}
        self.init_objects()
        if 'to_render' in self.groups or 'main' in self.groups:
            exit(-1)
        main_group = Group()
        for group in self.groups.values():
            main_group.add(*group.sprites())
        self.groups['main'] = main_group
        self.groups['to_render'] = self.groups['main'].copy()

    # Добавить все игровые объекты в массив groups
    @abstractmethod
    def init_objects(self):
        pass

    def process_logic(self, events):
        for sprite in self.groups['main']:
            sprite.process_logic(events)

    def render(self):
        self.groups['to_render'].draw(self.game.screen)
