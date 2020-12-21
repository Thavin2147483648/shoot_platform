from enums import PositionX, PositionY, TextAlign
from models.Text import PositionalText


class ToExitText(PositionalText):
    GROUP_NAME = 'to_exit_text'

    def __init__(self, scene, *groups, position_x=PositionX.RIGHT, position_y=PositionY.TOP):
        super().__init__(scene, position_x, position_y, *groups, text="Press E\nto exit level", align=TextAlign.RIGHT)

    def can_exit(self):
        player = self.scene.get_object('player')
        for obj in self.scene.get_objects('exit'):
            if obj.collide_with(player):
                return True
        return False

    def process_logic(self, events):
        if self.can_exit():
            self.show()
        else:
            self.hide()
