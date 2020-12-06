from models.Float import Float


def is_intersection(r1, r2):  # r1, r2 = (x1, y1, x2, y2);
    # (x1, y1) - левый верхний угол, (x2, y2) - правый нижний
    return not (Float(r2[3]) <= Float(r1[1]) or Float(r2[0]) >= Float(r1[2]) or
                Float(r2[1]) >= Float(r1[3]) or Float(r2[2]) <= Float(r1[0]))


def rect_collide(a, b):
    return is_intersection((a.x, a.y, a.x + a.width, a.y + a.height),
                           (b.x, b.y, b.x + b.width, b.y + b.height))


def get_sign(n):
    if n >= 0:
        return 1
    return -1


def custom_round(n):
    return int(get_sign(n) * round(abs(n)))
