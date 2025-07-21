import pygame as pg
pg.init()
Width = 200
Height = 400
px = 100
ex = 100
screen = pg.display.set_mode((Width,Height))
direction = 'right'
while True : 
    
    for event in pg.event.get() :
        if event.type == pg.KEYDOWN : 
            if event.key == pg.K_RIGHT: 
                px = px + 3
            if event.key == pg.K_LEFT: 
                px = px - 3 
        if event.type == pg.QUIT :
            pg.quit() 
    screen.fill((0,0,0))
    player = pg.draw.rect(screen,pg.Color('blue'),(px,340,20,40))
    e1 = pg.draw.rect(screen,pg.Color('red'),(ex,40,60,40))
#enemy movement
    if direction == 'right' :
        ex = ex + 0.005
        if ex >= 198 : 
            direction = 'left'
    if direction == 'left' :
        ex = ex - 0.005 
        if ex <= 0 :
            direction = 'right'


    pg.display.update()
    





