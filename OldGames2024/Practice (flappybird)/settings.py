import pygame as pg
from pygame.locals import *

pg.init()

screen_width = 864
screen_height = 936

screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Flappy Bird')

# LOAD images
bg = pg.image.load('img/bg.png')
run = True
while run == True : 
    for event in pg.event.get():
        if event.type == pg.QUIT :
            run == False

pg.quit()