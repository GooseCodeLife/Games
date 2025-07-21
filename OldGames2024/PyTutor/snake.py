import pygame as pg 
import random
clock = pg.time.Clock()
sbody = [[100,50],[90,50],[80,50],[70,10]]
run = True
test_surface = pg.Rect(random.randint(0,400),random.randint(0,400),60,100)
y_pos = 50
x_pos = 100
screen = pg.display.set_mode((400,400))
pos = 0
direction = 'down'
speed = 10
x_food = 50
y_food = 50
food = pg.Rect
score = 0


pg.init()
pg.font.init()
font = pg.font.Font(None,36)
score_text = font.render(f'Score {str(score)}',True,pg.Color('White'))

while True : 
    for event in pg.event.get():
        if event.type == pg.KEYDOWN : 
            if event.key == pg.K_UP :
                direction = 'up'
            if event.key == pg.K_DOWN : 
                direction = 'down'
            if event.key == pg.K_RIGHT : 
                direction = 'right'
            if event.key == pg.K_LEFT : 
                direction = 'left'

        if event.type == pg.QUIT :
            pg.quit()
            sys.exit() 
    if x_pos > 400 or y_pos > 400 :
        pg.quit()
    pos = pos +0.02 
    if direction == 'left' :
        x_pos = x_pos - speed
    if direction == 'right' :
        x_pos = x_pos + speed
    if direction == 'up' :
        y_pos = y_pos - speed
    if direction == 'down' :
        y_pos = y_pos + speed
    screen.fill((0,0,0))
    sbody.insert(0,[x_pos,y_pos])
    if abs(x_food-x_pos) < 5  and abs(y_food- y_pos) < 5  : 
        score = score + 1
        score_text = font.render(f'Score {str(score)}',True,pg.Color('White'))
        x_food = random.randint(0,400)
        y_food = random.randint(0,400)
        print('You got food')
    else : 
        sbody.pop()
    food = pg.draw.rect(screen,pg.Color('red'),pg.Rect(x_food,y_food,10,10))
    #pg.draw.ellipse(screen,pg.Color('purple'),pg.Rect(random.randint(0,400),random.randint(0,400),60,100))
    for i in sbody :
        pg.draw.rect(screen,pg.Color('purple'),pg.Rect(i[0],i[1],10,10))
    
    pg.display.update() 
    clock.tick(speed)


