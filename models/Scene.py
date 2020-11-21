from abc import ABC, abstractmethod


class Scene(ABC):
    def __init__(self, game, index):
        self.game = game
        self.index = index
        self.objects = []
        self.objects_dct = {}
        self.init_objects()
        for obj in self.objects:
            if obj.name in self.objects_dct:
                exit(-1)
            self.objects_dct[obj.name] = obj
        self.objects.sort(key=lambda x: x.index)

    # Добавить все игровые объекты в массив objects
    @abstractmethod
    def init_objects(self):
        pass

    def process_logic(self, events):
        for obj in self.objects:
            obj.process_logic(events)

    def render(self):
        for obj in self.objects:
            obj.render(self.game.screen)
