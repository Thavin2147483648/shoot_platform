import pygame as pg
from models.LevelObject import StaticLevelObject
from enums import LevelObjectCellPositionX as PositionX, LevelObjectCellPositionY as PositionY
from constants import Player, PlayerSpawn as Properties


class PlayerSpawn(StaticLevelObject):
    WIDTH = Properties.WIDTH
    HEIGHT = Properties.HEIGHT
    ANIMATION = Properties.IMAGE_PATH
    GROUP_NAME = 'player_spawn'
