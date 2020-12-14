from constants import Coin as Properties
from models.BonusItem import BonusItem


class Coin(BonusItem):
    WIDTH = Properties.WIDTH
    HEIGHT = Properties.HEIGHT
    ANIMATION = Properties.IMAGE_PATH
    GROUP_NAME = 'coin'

    def on_pickup(self):
        self.scene.get_object('score').add(Properties.SCORE_ADD)
