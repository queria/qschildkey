import pygame as pg
import color


class Symbol(pg.Surface):
    def __init__(self, width, height):
        super(Symbol, self).__init__((width, height), flags=pg.SRCALPHA)


class Invalid(Symbol):
    def __init__(self):
        super(Invalid, self).__init__(200, 200)
        pg.draw.aaline(self, (0, 0, 255), (0, 0), (200, 200))
        pg.draw.aaline(self, (0, 0, 255), (200, 0), (0, 200))


class Number(Symbol):
    def __init__(self, count=0):
        self.count = count
        space = 10
        width = 100

        super(Number, self).__init__(
            max(1, count*(width+space) - space), 100)

        for r in xrange(self.count):
            pg.draw.rect(self, color.GREEN,
                        (r*(width+space), 0,
                         width, width))


class Rectangle(Symbol):
    def __init__(self, clr=None):
        super(Rectangle, self).__init__(200, 200)
        self.color = clr or color.RED
        pg.draw.rect(self, self.color, (0, 0, 200, 200), 0)


class Car(Symbol):
    def __init__(self):
        super(Car, self).__init__(400, 200)
        c = color.BLACK
        outline = [(10, 160), (10, 180),                # |
                   (50, 180),                           # -
                   (50, 190), (65, 197), (75, 197), (90, 190),     # \_/
                   (90, 180), (170, 180),
                   (170, 190), (185, 197), (195, 197), (210, 190),    # \_/
                   (210, 180), (250, 180)]
        draw_lines(self, c, outline)
        #pg.draw.aaline(self, c, (


def Picture(name):
    return pg.image.load('./img/{0}.png'.format(name))


def draw_lines(sfc, clr, point_list):
    last_p = None
    for p in point_list:
        if last_p is not None:
            pg.draw.aaline(sfc, clr, last_p, p)
        last_p = p
