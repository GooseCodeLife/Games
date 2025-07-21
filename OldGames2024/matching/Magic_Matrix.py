import pygame as pg 
import random 
import time 
screen = pg.display.set_mode((260,260))
Boxes = []
blue_box = []
#font = pg.font.Font('Ariel', 32)
pg.init()
pg.font.init()
font = pg.font.SysFont('Times', 20)
amount = 4
#loading image
Grey_Box = pg.image.load('Grey_Square.png').convert_alpha()
Blue_Box = pg.image.load('Blue_Box.png').convert_alpha()
#class
class Box (pg.sprite.Sprite) :
    def __init__ (self,Grey,Blue,x,y):
        super().__init__() 
        self.x = x 
        self.y = y 
        self.Grey = Grey
        self.Blue = Blue
        self.hide = True
    def draw (self,screen) :
        if self.hide == True :
            screen.blit(self.Grey,(self.x,self.y))
        else : 
            #pg.draw.rect(screen, pg.Color('black'),pg.Rect(self.x, self.y, 50, 50))
            screen.blit(self.Blue,(self.x,self.y))
    def hit (self,mx,my) :
        if mx>=self.x  and mx <= self.x+ 30   : 
            if my >= self.y and my <= self.y + 30 : 
                return True
    def appear (self) : 
        self.hide == False

#function
def game(amount) : 
    blue_box = []
    for i in range(amount) : 
        blue_box.append(random.randint(0,24))
    print(blue_box)
    for row in range (5) : 
        for column in range (5) :
            if 5*row+column+1 in blue_box : 
                box = Box(Blue_Box,Grey_Box,10+row*40,10+column*40)
            else :
                box = Box(Grey_Box,Blue_Box,10+row*40,10+column*40)
            box.draw(screen)
            
    pg.display.update()
    time.sleep(2)
    for row in range (5) : 
        for column in range (5) :
            box = Box(Grey_Box,Blue_Box,10+row*40,10+column*40,)
            box.draw(screen)
            Boxes.append(box)
    pg.display.update()

#turn back to gray

        #text = font.render('GeeksForGeeks', True, green, blue)

text = font.render('You Lost!',True,pg.Color('white'))
textrect = text.get_rect()
textrect.center = (50,50)
game(amount)
pg.display.update()
#5xrow+column+1

while True : 
    for event in pg.event.get() :
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONUP:
            mx,my = pg.mouse.get_pos()
            print(mx,my)
            #print(Boxes)

            for box in Boxes :
                if box.hit(mx,my) :
                    box.appear()
                    box.draw(screen)
                    x = mx - 10
                    y = my - 10 
                    x = x //40 
                    y = y // 40 
                    the_box = 5*x + y + 1 
                    if the_box in blue_box : 
                        blue_box.remove(the_box)
                    else : 
                        print('YOU LOSE')
                        losing_Screen =pg.draw.rect(screen, pg.Color('black'),pg.Rect(0, 0, 260, 260)  ) 
                        screen.blit(text,textrect )
                        if amount > 2 : 
                            amount = amount - 1 
                        game(amount)

                    if len(blue_box) == 0 : 
                        print('You WIN')
                        if amount < 2 :
                            amount = amount + 1
                        game(amount)
                    print(the_box,x,y)  

    pg.display.update()

