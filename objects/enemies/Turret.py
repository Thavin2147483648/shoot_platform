from models.LevelObject import StaticLevelObject
from constants import Turret as Properties
from enums import DirectionX


class Turret(StaticLevelObject):
    WIDTH = Properties.WIDTH
    HEIGHT = Properties.HEIGHT
    EXTRA_WIDTH = 52
    ANIMATION = Properties.ANIMATION
    CAN_COLLIDE = True
    GROUP_NAME = 'turret'

    def __init__(self, scene, cell_x, cell_y, *groups):
        super().__init__(scene, cell_x, cell_y, *groups)
        self.extra_width = self.EXTRA_WIDTH
        self.direction_x = DirectionX.LEFT

    def process_logic(self, events):
        player = self.scene.get_object('main_character')
        if player.get_middle_x() <= self.get_middle_x():
            self.direction_x = DirectionX.LEFT
        else:
            self.direction_x = DirectionX.RIGHT
        d = ('left' if self.direction_x == DirectionX.LEFT else 'right')
        self.animation.set_animation('none_' + d)

    def get_extra_width(self):
        return self.extra_width

    def get_render_rect(self):
        rect = super(Turret, self).get_render_rect()
        rect.width += self.get_extra_width()
        if self.direction_x == DirectionX.LEFT:
            rect.x -= self.get_extra_width()
        return rect
