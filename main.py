#!/usr/bin/python

import sys
import pygame as pg
import color
import config


def event2symbol(event, use_invalid):
    if event.type == pg.KEYDOWN:
        if event.key in config.symbols:
            return config.symbols[event.key]
        if use_invalid:
            return config.symbols['default']
    return None


def is_for_quit(event):
    return (
        event.type == pg.QUIT
        or (event.type == pg.KEYDOWN
            and event.key == pg.K_q
            and (event.mod & pg.KMOD_CTRL) != 0
            and (event.mod & pg.KMOD_ALT) != 0)
    )


def main():
    scr = pg.display.set_mode((800, 600))
    modes = pg.display.list_modes()
    if len(modes) > 0:
        pg.display.set_mode(modes[0], pg.FULLSCREEN | pg.HWSURFACE)
    clock = pg.time.Clock()
    running = True
    last_symbol = None
    use_invalid = '--invalid' in sys.argv

    while running:
        for event in pg.event.get():
            if is_for_quit(event):
                running = False
            last_symbol = event2symbol(event, use_invalid) or last_symbol

        scr.fill(color.DARKGRAY)
        if last_symbol is not None:
            scr.blit(last_symbol, (0, 0))
        pg.display.flip()
        clock.tick(50)


if __name__ == '__main__':
    main()
