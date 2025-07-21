import pygame as pg 
from pygame.locals import * 
pg.init() 
screen_width = 1000 
screen_height = 1000
screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption('Platformer')

#define game variables
tile_size = 200 

#load imgs
sun_img = pg.image.load('img/sun.png')
bg_img = pg.image.load('img/sky.png')

def draw_grid():
	for line in range(0, 20):
		pg.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pg.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

run = True
while run : 

    screen.blit(bg_img, (0,0))
    screen.blit(sun_img, (100,100))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update() 
pg.quit() 