from abc import ABC, abstractmethod

from pygame.sprite import Group

from constants import Basic


class Scene(ABC):
    def __init__(self, game, index):
        self.game = game
        self.index = index
        self.to_render = []
        self.groups = {}

    def reload(self):
        self.groups = {}
        self.init_objects()
        if 'main' in self.groups:
            exit(-1)
        main_group = Group()
        for group in self.groups.values():
            main_group.add(*group.sprites())
        self.groups['main'] = main_group
        self.to_render = []
        for i in range(Basic.RENDER_LEVELS):
            self.to_render.append(Group())
        for sprite in self.groups['main'].sprites():
            self.to_render[sprite.render_level].add(sprite)

    # Добавить все игровые объекты в массив groups
    @abstractmethod
    def init_objects(self):
        pass

    def get_object(self, name):
        return self.groups[name].sprite

    def get_objects(self, name):
        return self.groups[name].sprites()

    def process_logic(self, events):
        for sprite in self.groups['main']:
            sprite.process_logic(events)

    def render(self):
        self.groups['main'].update()
        for i in range(Basic.RENDER_LEVELS):
            self.to_render[i].draw(self.game.screen)
