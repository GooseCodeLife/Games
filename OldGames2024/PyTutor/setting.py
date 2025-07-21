import pygame as pg
import random
pg.Color

WIDTH = 400
HEIGHT  = 400
           
             
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.init()          
while True : 
    pg.draw.rect(screen, pg.Color(255,255,255),pg.Rect(random.randint(0,1000),random.randint(0,1000),10,10))
    screen.blit()


    pg.display.update() 
    FPS = pg.time.Clock() 


