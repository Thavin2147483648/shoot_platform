from constants import Basic


class Float(float):
    EPS = Basic.EPS

    def __eq__(self, other):
        return abs(float(self) - float(other)) < self.EPS

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self != other and float(self) < float(other)

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return self != other and float(self) > float(other)

    def __ge__(self, other):
        return self == other or self > other

    def __int__(self):
        return int(round(float(self)))
