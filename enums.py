from enum import Enum


class TextAlign(Enum):
    LEFT = 0
    CENTER = 1
    RIGHT = 2


class TextPositionX(Enum):
    LEFT = 0
    MIDDLE = 1
    RIGHT = 2


class TextPositionY(Enum):
    TOP = 0
    MIDDLE = 1
    BOTTOM = 2


class LevelObjectCellPositionX(Enum):
    LEFT = 0
    MIDDLE = 1
    RIGHT = 2


class LevelObjectCellPositionY(Enum):
    TOP = 0
    MIDDLE = 1
    BOTTOM = 2


class DirectionX(Enum):
    LEFT = 0
    NONE = 1
    RIGHT = 2
