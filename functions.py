from pygame import Rect


def is_intersection(r1, r2):  # r1, r2 = (x1, y1, x2, y2);
    # (x1, y1) - левый верхний угол, (x2, y2) - правый нижний
    return not (r2[3] < r1[1] or r2[0] > r1[2] or r2[1] > r1[3] or r2[2] < r1[0])


def rect_collide(r1, r2):
    a = tuple()
    b = tuple()
    if type(r1) is tuple or type(r1) is list:
        a = Rect(r1)
    if type(r2) is tuple or type(r2) is list:
        b = Rect(r2)
    return is_intersection((a.x, a.y, a.x + a.width - 1, a.y + a.height - 1),
                           (b.x, b.y, b.x + b.width - 1, b.y + b.height - 1))


def get_sign(n):
    if n >= 0:
        return 1
    return -1


def custom_round(n):
    return int(get_sign(n) * round(abs(n)))
