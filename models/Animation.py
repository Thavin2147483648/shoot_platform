import pygame as pg

from models.GameObject import GameObject


class Animation:
    """
    dct - словарь вида:
    название_анимации: ((изображение_1, длительность_1*), (изображение_2, длительность_2*), ...,
                        (изображение_n, длительность_n*))
    * длительность измеряется в количестве кадров
    """
    def __init__(self, obj: GameObject, dct: [dict, str], current='none'):
        self.dct = {}
        self.override_animations(dct)
        self.obj = obj
        self.current_name = ''
        self.start = 0
        self.pointer = 0
        self.frames_cnt = 0
        self.current = None
        self.set_animation(current)

    def get_frames(self):
        return self.obj.scene.game.get_frames()

    def override_animations(self, dct):
        if type(dct) is str:
            dct = {'none': ((dct, 1),)}
        for name in dct:
            self.override_animation(name, dct[name])

    def override_animation(self, name, value):
        arr = []
        print('value =', value)
        for i in value:
            arr.append((pg.image.load(i[0]), i[1]))
        self.dct[name] = tuple(arr)

    def set_animation(self, animation):
        if self.get_animation() == animation:
            return
        self.current_name = animation
        self.current = self.dct[animation]
        self.start = self.get_frames()
        self.pointer = 0
        self.frames_cnt = 0

    def get_animation(self):
        return self.current_name

    def get_current_image(self):
        return self.current[self.pointer][0]

    def update(self):
        self.frames_cnt += 1
        if self.frames_cnt >= self.current[self.pointer][1]:
            self.pointer = (self.pointer + 1) % len(self.current)
            self.frames_cnt = 0
        return self.get_current_image()
