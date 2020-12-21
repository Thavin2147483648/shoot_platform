import pygame as pg

from functions import get_surface
from models.BarIndicator import BarIndicatorColor
from models.Float import Float
from models.GameObject import PositionalGameObject
from models.BarIndicator import BarIndicator
from enums import PositionX, PositionY
from constants import HealthIndicator as Properties, Player


class HealthIndicator(PositionalGameObject):
    WIDTH = Properties.ICON_WIDTH + Properties.ICON_BAR_OFFSET + Properties.BAR_WIDTH
    HEIGHT = max(Properties.ICON_HEIGHT, Properties.BAR_HEIGHT)
    GROUP_NAME = 'health_indicator'

    def __init__(self, scene, *groups, position_x=PositionX.LEFT, position_y=PositionY.BOTTOM,
                 current=Player.HEALTH):
        super().__init__(scene, position_x, position_y, *groups)
        bar_color = BarIndicatorColor(*Properties.BAR_COLOR)
        self.max = Player.HEALTH
        self.current = current
        self.icon = pg.image.load(Properties.ICON_IMAGE)
        self.icon_width = Properties.ICON_WIDTH
        self.icon_height = Properties.ICON_HEIGHT
        self.icon_bar_offset = Properties.ICON_BAR_OFFSET
        self.bar = BarIndicator(Properties.BAR_WIDTH, Properties.BAR_HEIGHT, bar_color, Properties.BAR_BORDER_SIZE,
                                Player.HEALTH, current)
        self.set_current(self.current)

    def update_surface(self):
        self.bar.set_current(self.current)
        image = get_surface(self.width, self.height)
        image.blit(self.icon, (0, (self.height - self.icon_height) // 2))
        image.blit(self.bar.get_image(), (self.icon_width + self.icon_bar_offset, (self.height - self.bar.height) // 2))
        self.set_image(image)
        self.update_position()

    def set_current(self, current):
        if 0 <= current <= self.max:
            self.current = current
            self.update_surface()

    def get_current(self):
        return Float(self.current)

    def process_logic(self, events):
        player = self.scene.get_object('player')
        if player.get_health() != self.get_current():
            self.set_current(player.get_health())
