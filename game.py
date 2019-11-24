import pygame as pg
import time, settings, sys

pg.init()

screen=pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
pg.display.set_caption("agario")
clock =pg.time.Clock()





running = True
while running:
    clock.tick(settings.FPS)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()
    screen.fill(settings.colors["BLUE"])

    pg.display.flip()

pg.quit()





