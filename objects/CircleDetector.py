from constants import Color
from functions import get_surface
from models.Float import Float
from models.LevelObject import LevelObject
from functions import circle_and_rect_collide


class CircleDetector(LevelObject):
    def __init__(self, scene, a: float, b: float, radius: float, *groups):
        super().__init__(scene, a - radius, b - radius, *groups, render_level=1)
        self.a = a
        self.b = b
        self.radius = radius
        self.width = int(Float(2 * self.radius))
        self.height = int(Float(2 * self.radius))
        image_red = get_surface(self.width, self.height)
        image_green = get_surface(self.width, self.height)
        for x in range(self.width):
            for y in range(self.height):
                if circle_and_rect_collide((Float(x + self.x), Float(y + self.y), Float(x + self.x + 1),
                                            Float(y + self.y + 1)),
                                           (self.a, self.b, self.radius)):
                    image_red.set_at((x, y), Color.RED)
                    image_green.set_at((x, y), Color.GREEN)
        dct = {
            'none': ((image_red, 1),),
            'detected': ((image_green, 30), (image_red, 30))
        }
        self.animation.override_animations(dct)

    def get_circle(self):
        return self.a, self.b, self.radius

    def circle_collide_with(self, obj):
        return circle_and_rect_collide(obj.get_rect(), self.get_circle())

    def process_logic(self, events):
        if self.circle_collide_with(self.scene.get_object('main_character')):
            self.animation.set_animation('detected')
        else:
            self.animation.set_animation('none')
