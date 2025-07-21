import pygame as pg
import random
import math 
from math import * 
pg.init() 
screen = pg.display.set_mode((500,500))
clock = pg.time.Clock()


#sun pos
xpos = 220
ypos = 220
#1
x = 50
y= 50
#2
jx = 50
jy = 50
#3
ex = 50
ey = 50
#4
mx = 50
my = 50
#5
jx = 50
jy = 50
#6
sx = 50
sy = 50
#7 
ux = 50
uy = 50
#8
nx = 50
ny = 50
#angles
anglem = 0.1
anglev = 0.3
anglee = 0.4
anglema = 0.5
anglej = 0.6
angles = 0.7
angleu = 0.8
anglen = 0.9
while True:
    for event in pg.event.get() : 
        if event.type == pg.QUIT :
            pg.QUIT
    
    screen.fill((0,0,0))
    #1
    x = xpos + 100*cos(anglem)
    y = ypos + 100*sin(anglem)
    #2
    jx = xpos + 125*cos(anglev)
    jy = ypos + 125*sin(anglev)
    #3
    ex = xpos + 150*cos(anglee)
    ey = ypos + 150*sin(anglee)
    #4
    mx = xpos + 175*cos(anglema)
    my = ypos + 175*sin(anglema)
    #5
    jx = xpos + 220*cos(anglej)
    jy = ypos + 220*sin(anglej)
    #6
    sx = xpos + 240*cos(angles)
    sy = ypos + 240*sin(angles)
    #7 
    ux = xpos + 260*cos(angleu)
    uy = ypos + 260*sin(angleu)
    #8
    nx = xpos + 280*cos(anglen)
    ny = ypos + 280*sin(anglen)
    #angles
    anglem = anglem + 0.5
    anglev = anglev + 0.3
    anglee = anglee + 0.1
    anglema = anglema + 0.07
    anglej = anglej + 0.2
    angles = angles + 0.18
    angleu = angleu + 0.16
    anglen = anglen + 0.05
    #planets
    sun = pg.draw.ellipse(screen,pg.Color('yellow'),pg.Rect(xpos,ypos,70,70))
    mercury = pg.draw.ellipse(screen,pg.Color('brown'),pg.Rect(x,y,20,20))
    venus = pg.draw.ellipse(screen,pg.Color('red'),pg.Rect(jx,jy,30,30))
    earth = pg.draw.ellipse(screen,pg.Color('green'),pg.Rect(ex,ey,40,40))
    mars = pg.draw.ellipse(screen,pg.Color('red'),pg.Rect(mx,my,30,30))
    jupiter = pg.draw.ellipse(screen,pg.Color('yellow'),pg.Rect(jx,jy,40,40))
    saturn = pg.draw.ellipse(screen,pg.Color('brown'),pg.Rect(sx,sy,50,50))
    uranus = pg.draw.ellipse(screen,pg.Color('red'),pg.Rect(ux,uy,40,40))
    neptune = pg.draw.ellipse(screen,pg.Color('blue'),pg.Rect(nx,ny,40,40))
    #updates
    pg.display.update()
    clock.tick(10)