from models.Text import Text


class Score(Text):
    def __init__(self, scene, x, y, start_score=0, *groups):
        super().__init__(scene, x, y, *groups)
        self.current = start_score
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
        self.set_text('SCORE: ' + str(self.current))
        super().update(*args, **kwargs)
