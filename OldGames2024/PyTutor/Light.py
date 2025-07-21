#light
import pygame as pg
pg.init() 
WIDTH = 175
HEIGHT = 400
screen = pg.display.set_mode((WIDTH,HEIGHT)) 
#variables
epos1 = -10
epos2x = 60
epos2 = 10
direction = 'right'
arkstart = 1.7
arkstop = 3.4
arkeposy = 30
arkx = 30

while True : 
    for event in pg.event.get() :
        if event.type == pg.QUIT : 
            pg.quit() 
    screen.fill((0,0,0))
    pos = pg.mouse.get_pos()  
    player = pg.draw.circle(screen,pg.Color('white'),[pos[0],pos[1]],5,5)
    enemy1 = pg.draw.rect(screen,pg.Color('blue'),pg.Rect(20,epos1,106,10))
    eacross = pg.draw.rect(screen,pg.Color('blue'),pg.Rect(epos2x,epos2,75,10))
    eark = pg.draw.arc(screen,pg.Color('blue'),pg.Rect(arkx,arkeposy,60,60),arkstart,arkstop,6)
#enemies moving y value
    epos1 = epos1 + 0.00
    epos2 = epos2 + 0.00
    arkeposy = arkeposy + 0.005
    arkstart = arkstart - 0.0005
    arkstop = arkstop - 0.0005
#enemy 2 direction
    if direction == 'right':
        epos2x = epos2x + 0.005
        if epos2x >= 110 :
            direction = 'left'
    if direction == 'left' :
        print(direction)
        epos2x = epos2x - 0.005
        if epos2x <= 0 :
            direction = 'right'
#enemy respawn
    if epos1 >= 400:
        epos1 = -20 
    if epos2 >= 400:
        epos2 = -30
    if arkeposy >= 400:
        arkeposy = -100
#enemy1 die
    if abs(epos1 - pos[1]) <15 and 20 < pos[0] < 126: 
        exit()
#enemy2 die
    if abs(epos2 - pos[1]) < 15 and epos2x < pos[0] < epos2x + 75 :
        exit()
#ark die
    if abs(arkeposy - pos[1]) < 15  and arkx < pos[0] < arkx + 30:
        exit()
    pg.display.update()



