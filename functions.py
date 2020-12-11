import pygame as pg
from models.Float import Float


def is_intersection(r1, r2):  # r1, r2 = (x1, y1, x2, y2);
    # (x1, y1) - левый верхний угол, (x2, y2) - правый нижний
    return not (Float(r2[3]) <= Float(r1[1]) or Float(r2[0]) >= Float(r1[2]) or
                Float(r2[1]) >= Float(r1[3]) or Float(r2[2]) <= Float(r1[0]))


def rect_collide(a, b):
    return is_intersection((a.x, a.y, a.x + a.width, a.y + a.height),
                           (b.x, b.y, b.x + b.width, b.y + b.height))


# circle: tuple(a, b, radius)
# rect: tuple(x1, y1, x2, y2)
def circle_and_rect_collide(rect, circle):
    def subf(segment: tuple, coord: float):
        if Float(segment[0]) <= Float(coord) <= Float(segment[1]):
            return 0
        return min(Float((coord - segment[0]) ** 2), Float((coord - segment[1]) ** 2))
    return Float(subf((rect[0], rect[2]), circle[0]) + subf((rect[1], rect[3]), circle[1])) < Float(circle[2] ** 2)


def get_sign(n):
    if n >= 0:
        return 1
    return -1


def get_surface(width, height):
    surface = pg.Surface((width, height), pg.SRCALPHA)
    surface.fill((0, 0, 0, 0))
    return surface


def custom_round(n):
    return int(get_sign(n) * round(abs(n)))
