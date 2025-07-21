import pygame as pg 
import random

# activate the pygame library .
pg.init()
X = 600
Y = 600
 
# create the display surface object
# of specific dimension..e(X, Y).
scrn = pg.display.set_mode((X, Y))
 
# set the pygame window name
pg.display.set_caption('image')
 
# create a surface object, image is drawn on it.
imp = pg.image.load("d:\\kavya\\pytutor\\assets\\one.png").convert()
 
# Using blit to copy content from one surface to other
scrn.blit(imp, (0, 0))


# paint screen one time
pg.display.flip()
status = True
while (status):
 
  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for i in pg.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pg.QUIT:
            status = False
 
# deactivates the pygame library
pg.quit()
