
import pygame as pg 

pg.init 
Width = 300
Height = 300 
screen = pg.display.set_mode((Height,Width ))
#loading imgs
Blue = pg.image.load('Blue_Bubble.png').convert_alpha()
Red = pg.image.load('Red.png').convert_alpha()
#Red_rect = Red.get_frect(Height/2, Width/2)

class Bubble():
    def __init__ (self) : 
        super().__init__()
        
    #def draw(self) :
    def move (self ) :
        pass 
         
x = Width/2-20  
y = Height-60 
while True :
    mx,my = pg.mouse.get_pos()
    screen.blit(Blue, (x,y))
    screen.blit(Red, (0,0))
    # direction = (mx-x, my - y )   
    for event in pg.event.get() : 
        if event.type == pg.MOUSEBUTTONUP : 
            (mx,my) = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN : 
            pass 
        if event.type == pg.QUIT :
            pg.QUIT
    

    
    pg.display.update()
