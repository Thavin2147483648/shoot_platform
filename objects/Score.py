from models.Text import PositionalText
from constants import Score as Properties


class Score(PositionalText):
    def __init__(self, scene, *groups, position_x=Properties.POSITION_X,
                 position_y=Properties.POSITION_Y, offset=Properties.OFFSET, color=Properties.COLOR, start_score=0):
        super().__init__(scene, position_x, position_y, *groups, offset=offset, color=color)
        self.current = start_score
        self.max_score = self.scene.get_max_score()
        self.set_score(self.current)

    def get_current(self):
        return self.current

    def set_score(self, score):
        self.current = score
        self.update()

    def add(self, d):
        self.set_score(self.current + d)

    def get(self):
        return self.current

    def update(self, *args, **kwargs) -> None:
        self.set_text('SCORE: ' + str(self.current) + '\nMAX SCORE: ' + str(self.max_score))

        super().update(*args, **kwargs)
