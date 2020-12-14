from constants import Ammo as Properties
from models.BonusItem import BonusItem


class Ammo(BonusItem):
    WIDTH = Properties.WIDTH
    HEIGHT = Properties.HEIGHT
    ANIMATION = Properties.IMAGE_PATH
    GROUP_NAME = 'ammo_bonus'

    def on_pickup(self):
        weapon = self.scene.get_object('main_character').get_weapon()
        if weapon is not None:
            weapon.reload()

    def pickup_condition(self):
        weapon = self.scene.get_object('main_character').get_weapon()
        return weapon is not None and weapon.get_remaining() < weapon.CAPACITY
