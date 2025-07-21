#racing game
import pygame as pg
import random
pg.init()
pg.font.init()
font = pg.font.Font(None,36)
Width = 200
Height = 400
screen = pg.display.set_mode((Width, Height))
score = 0 
x_pos = 10
y_epos = 10
x_epos = 10
x_epos2 = 40
y_epos2 = 10
y_pos = 315
y_epos3 = 10
x_epos3 = 70
lose = False
score_text = font.render(f'Score {str(score)}',True,pg.Color('White'))
while True: 
    for event in pg.event.get():
        if event.type == pg.KEYDOWN : 
            if event.key == pg.K_RIGHT:
                x_pos = x_pos + 5
            if event.key == pg.K_LEFT : 
                x_pos = x_pos - 5
        if event.type == pg.QUIT:
            pg.quit()
    
    screen.fill((0,0,0))
    player = pg.draw.rect(screen,pg.Color('purple'),pg.Rect(x_pos,y_pos,20,60))
    y_epos = y_epos + 0.005
    y_epos2 = y_epos2 + 0.009
    y_epos3 = y_epos3 + 0.01
    enemy = pg.draw.rect(screen,pg.Color('red'),pg.Rect(x_epos,y_epos,20,60))
    enemy2 = pg.draw.rect(screen,pg.Color('orange'),pg.Rect(x_epos2,y_epos2,20,60))
    enemy3 = pg.draw.rect(screen,pg.Color('yellow'),pg.Rect(x_epos3,y_epos3,20,60))
    if y_epos3 >= 390 :
        y_epos3 = 10
        x_epos = random.randint(0,Width)
        score = score + 1
        if lose == False:
            score_text = font.render(f'Score {str(score)}',True,pg.Color('White'))
    if y_epos >= 390 : 
        y_epos = 10
        x_epos = random.randint(0,Width)
        score = score + 1
        if lose == False:
            score_text = font.render(f'Score {str(score)}',True,pg.Color('White'))
    if y_epos2 >= 356 :
        y_epos2 = 10
        x_epos2 = random.randint(0,Width)
        score = score + 1
        if lose == False :
            score_text = font.render(f'Score {str(score)}',True,pg.Color('White'))
    if x_pos <= 0 :
        x_pos = 0
    elif x_pos >= Width - 20 :
        x_pos = Width -20
    if abs(x_pos - x_epos) < 20 and abs(y_pos - y_epos ) < 20:
        y_pos = 500
        x_epos = 300
        x_epos2 = 300
        x_epos3 = 300
        lose = True
    elif abs(x_pos - x_epos2) < 20 and abs(y_pos - y_epos2 ) < 20:
        y_pos = 500
        x_epos = 300
        x_epos2 = 300
        x_epos3 = 300
        lose = True
    elif abs(x_pos - x_epos3) < 20 and abs(y_pos - y_epos3 ) < 20:
        y_pos = 500
        x_epos = 300
        x_epos2 = 300
        x_epos3 = 300
        lose = True
    if abs(x_epos-x_epos2) < 20 and abs(y_epos - y_epos2 ) < 20 :
        y_epos = 10 
        x_epos = random.randint(0,Width)
    if abs(x_epos - x_epos3) < 30 and abs(y_epos - y_epos3) < 20 :
        y_epos = 10
        x_epos = random.randint(0,Width)
    if abs(x_epos2 - x_epos3) < 30 and abs(y_epos2 - y_epos3) < 20 :
        y_epos2 = 10
        x_epos = random.randint(0,Width)
    screen.blit(score_text,(10,10))
    pg.display.update() 




