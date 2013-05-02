# -*- coding: utf-8

import pygame as pg
import symbol

symbols = {}
symbols['default'] = symbol.Invalid()
symbols[pg.K_1] = symbol.Number(1)
symbols[pg.K_2] = symbol.Number(2)
symbols[pg.K_3] = symbol.Number(3)
symbols[pg.K_4] = symbol.Number(4)
symbols[pg.K_5] = symbol.Number(5)
symbols[pg.K_6] = symbol.Number(6)
symbols[pg.K_7] = symbol.Number(7)
symbols[pg.K_8] = symbol.Number(8)
symbols[pg.K_9] = symbol.Number(9)
symbols[pg.K_0] = symbol.Number(0)
#symbols[pg.K_a] = symbol.Car()
#symbols[pg.K_x] = symbol.Rectangle(color.AQUA)
#symbols[pg.K_y] = symbol.Rectangle(color.FUCHSIA)

images = {
    'a': (('auto', 'car'),),
    'b': (('balon', 'ball'),),
    # c
    ## cesta, cihla, cirkus, citron, čáp
    'd': (('dum', 'house'),),
    # e
    # f
    # fazole?
    # g
    ## gramofon?
    'h': (('hodiny', 'clocks'),),
    # i
    'j': (('jablko', 'apple'),),
    'k': (('kočka', 'cat'),
          ('kolo', 'bicycle'),),
    'l': (('lokomotiva', 'train_engine'),
          ('lopata', 'shovel'),),
    'm': (('myš', 'mouse'),),
    # n
    ## nos
    # o
    ## opice
    'p': (('pití', 'drink'),
          ('pes', 'dog'),
          ('pán', 'man'),),
    # q
    'r': (('ředkvička', 'radish'),
          ('rohlík', 'kifli'),),
    's': (('sýr', 'cheese'),),
    't': (('talíř', 'dish'),),
    # u
    ## uterka
    'v': (('vlak', 'train'),),
    # w
    # x
    ## xylofon
    # y
    'z': (('zajíc', 'hare'),),
    ## zámek
}

for key in images:
    key_id = getattr(pg, 'K_{0}'.format(key))
    symbols[key_id] = symbol.Picture(images[key][0][1])
