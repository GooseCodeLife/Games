#move in a square
import pygame as pg 
pg.init()
x = 20
y = 20
screen = pg.display.set_mode((500,500))
clock = pg.time.Clock()

xVel = 0
yVel = 5
dir = 1
while True : 

    screen.fill((0,0,0))
    player = pg.draw.rect(screen,pg.Color('blue'),(x,y,40,40))

    x = x+ xVel
    y = y + yVel 

    if (y >=250 and x<= 25 ):
        xVel = 5
        yVel = 0

    if (y >=250 and x>=250 ):
        xVel = 0
        yVel = -5

    if (y < 25 and x>=250 ):
        xVel = -5
        yVel = 0

    if (y < 25 and x<25 ):
        xVel = 0
        yVel = 5
        

    clock.tick(30)
    pg.display.update()




