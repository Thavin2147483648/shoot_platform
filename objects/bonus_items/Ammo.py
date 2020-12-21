from constants import Ammo as Properties
from models.BonusItem import BonusItem


class Ammo(BonusItem):
    WIDTH = Properties.WIDTH
    HEIGHT = Properties.HEIGHT
    ANIMATION = Properties.IMAGE_PATH
    GROUP_NAME = 'ammo_bonus'

    def on_pickup(self):
        weapon = self.scene.get_object('player').get_weapon()
        weapon.reload()

    def pickup_condition(self):
        weapon = self.scene.get_object('player').get_weapon()
        return weapon.get_remaining() < weapon.CAPACITY
