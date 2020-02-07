# pygame intro (setting up screen)
import pygame as pg
import sys
#------settings--------
FPS=30
colors_dict={}
colors_dict["red"]=(255, 0,0); colors_dict["green"]=(0,255,0); colors_dict["blue"]=(0,0, 255)
WIDTH= 400; HEIGHT=400

#----code for screen------
pg.init()
screen=pg.display.set_mode=((WIDTH, HEIGHT))#HEIGHT & WIDTH should be inserted as a tuple

#but this is not enough; the screen will flash and disappear
#we need a game loop to keep window open
running = True
while running:
  #---2-------
  for event in event.get():
    if event.type==pg.QUIT:
      sys.exit()#or running =False
  #----1-------
  #don't put this in "for event" loop
  pg.display.update()
  screen.fill((colors_dict["red"]))
  pg.display.flip()
pg.quit()
  
  
