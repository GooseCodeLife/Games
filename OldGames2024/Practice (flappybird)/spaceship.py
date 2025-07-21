
import pygame as pg
pg.init()
Width = 200
Height = 400
px = 100
ex = 100
x = 130
y = 70
ax = 450
ay = 340
shoot = 'False'
screen = pg.display.set_mode((Width,Height))
direction = 'right'
while True : 
    
    for event in pg.event.get() :
        if event.type == pg.KEYDOWN : 
            if event.key == pg.K_RIGHT: 
                px = px + 5
            if event.key == pg.K_LEFT: 
                px = px - 5 
            if event.key == pg.K_SPACE : 
                ax = px +5
                shoot = 'True'
                if ay <= 0:
                    ay = 340
        if event.type == pg.QUIT :
            pg.quit() 
    screen.fill((0,0,0))
    player = pg.draw.rect(screen,pg.Color('blue'),(px,340,20,40))
    e1 = pg.draw.rect(screen,pg.Color('red'),(ex,40,60,40))
    eammo = pg.draw.rect(screen,pg.Color('purple'),(x,y,10,10)) 
    ammo = pg.draw.rect(screen,pg.Color('green'),(ax,ay,10,10))
#enemy movement
    if direction == 'right' :
        ex = ex + 0.004              
        if ex >= 140 : 
            direction = 'left'
    if direction == 'left' :
        ex = ex - 0.004
        if ex <= 0 :
            direction = 'right'
    #enemy ammo move
    y = y + 0.01
    if y >= 400 : 
        y = 70
        x = ex
    #die
    if abs(px - x) < 15 and y > 340 :
        px = 900
        pg.QUIT
    #attack 
    if shoot == 'True':
        ay = ay - 0.03

    if abs(ex - ax) < 15 and ay < 20 :
        ex = 800
        pg.QUIT
    pg.display.update()






