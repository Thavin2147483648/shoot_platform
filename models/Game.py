import pygame as pg
from constants import Screen, Basic, Color
from scenes.Main import Main as MainScene


class Game:
    def __init__(self):
        self.scene_index = 0
        self.screen = None
        self.scenes = []
        self.frames_cnt = 0

    def init(self):
        pg.init()
        self.screen = pg.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
        pg.display.set_caption(Basic.NAME)
        self.screen.fill(Color.WHITE)
        self.scenes = [MainScene(self, 0, 200, 100, 'main_character')]
        self.scenes.sort(key=lambda x: x.index)

    def move_to_scene(self, index):
        self.scene_index = index

    def move_to_next_scene(self):
        self.move_to_scene((self.scene_index + 1) % len(self.scenes))

    def change_background_color(self, color):
        self.screen.fill(color)

    def get_scene(self):
        return self.scenes[self.scene_index]

    def update(self):
        t = pg.time.get_ticks()
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                exit()
        self.screen.fill(Color.WHITE)
        self.get_scene().process_logic(events)
        self.get_scene().render()
        pg.display.flip()
        self.frames_cnt += 1
        pg.time.delay(Basic.FRAME_DELAY - (pg.time.get_ticks() - t))

    def get_frames(self):
        return self.frames_cnt
