from functions import get_surface
from models.BarIndicator import BarIndicator, BarIndicatorColor
from models.Float import Float
from models.LevelObject import LevelObject
from constants import ObjectHealthIndicator as Properties


class ObjectHealthIndicator(LevelObject, BarIndicator):
    WIDTH = Properties.WIDTH
    HEIGHT = Properties.HEIGHT
    GROUP_NAME = 'object_health_indicator'

    def __init__(self, scene, obj, *groups, offset_y=Properties.OFFSET_Y):
        super().__init__(scene, 0, 0, *groups, render_level=3)
        self.obj = obj
        BarIndicator.__init__(self, Properties.WIDTH, Properties.HEIGHT, BarIndicatorColor(*Properties.BAR_COLOR),
                              Properties.BORDER_SIZE, obj.get_max_health(), obj.get_health())
        self.offset_y = Float(offset_y)

    def update_pos(self):
        self.set_middle_x(self.obj.get_middle_x())
        self.set_y2(self.obj.get_y1() - self.offset_y)

    def set_current(self, value):
        super().set_current(value)
        self.set_image(self.get_image())

    def process_logic(self, events):
        if self.get_current() != self.obj.get_health():
            self.set_current(self.obj.get_health())
        self.update_pos()
