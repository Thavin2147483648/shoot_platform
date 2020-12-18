from abc import ABC, abstractmethod

from pygame.sprite import Group

from constants import Basic


class Scene(ABC):
    def __init__(self, game, index):
        self.game = game
        self.index = index
        self.to_render = []
        self.groups = {}
        self.reload()

    def reload(self):
        self.groups = {
            'main': Group()
        }
        self.to_render = []
        for i in range(Basic.RENDER_LEVELS):
            self.to_render.append(Group())
        self.init_objects()

    def add_object(self, obj):
        self.groups['main'].add(obj)
        if obj.GROUP_NAME not in self.groups:
            self.groups[obj.GROUP_NAME] = Group()
        self.groups[obj.GROUP_NAME].add(obj)
        self.to_render[obj.render_level].add(obj)

    # Добавить все игровые объекты в массив groups
    @abstractmethod
    def init_objects(self):
        pass

    def get_object(self, name):
        return self.get_objects(name)[0]

    def get_objects(self, name):
        return self.groups[name].sprites()

    def object_exists(self, name):
        return name in self.groups

    def get_group(self, name):
        return self.groups.get(name, Group())

    def process_logic(self, events):
        for sprite in self.groups['main']:
            sprite.process_logic(events)

    def render(self):
        self.groups['main'].update()
        for i in range(Basic.RENDER_LEVELS):
            self.to_render[i].draw(self.game.screen)
