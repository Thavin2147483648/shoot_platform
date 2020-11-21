from constants import Screen
from models.Scene import Scene
from objects.MainCharacter import MainCharacter
from objects.Platform import Platform


class Main(Scene):
    def init_objects(self):
        self.objects += [MainCharacter(self, 0, 'main_character')]
        w = 150
        h = 165
        ground_h = 50
        self.objects.append(Platform(self, 1, 'platform_ground', (0, Screen.HEIGHT - ground_h),
                                     (Screen.WIDTH, ground_h)))
        n = Screen.WIDTH // w
        for i in range(n):
            self.objects.append(Platform(self, 2 + i, 'platform' + str(i),
                                         (w * i, Screen.HEIGHT - ground_h - h - h * (i % 2)), (w, 10)))
