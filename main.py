import pygame as pg
from models.Game import Game


def main():
    game = Game()
    game.init()
    while True:
        game.update()


if __name__ == '__main__':
    main()
