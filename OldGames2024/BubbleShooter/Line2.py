import pygame as pg 
pg.init 
Width = 300
Height = 300 
screen = pg.display.set_mode((Height,Width ))
#loading imgs
Blue = pg.image.load('Blue_Bubble.png').convert_alpha
Red = pg.image.load('Red.png').convert_alpha
#Red_rect = Red.get_rect(Height/2, Width/2)

class Bubble():
    def __init__ (self) : 
        super().__init__()
        
    #def draw(self) :
    def move (self ) :
        pass 
         
mx=0
my=0

while True :
    #screen.blit()
    screen.fill((255, 255, 255))

    #screen.blit(Red, Red_rect,)
    for event in pg.event.get() : 
        if event.type == pg.MOUSEMOTION : 
            (mx,my) = pg.mouse.get_pos()
            print(mx,my)
       
        if event.type == pg.QUIT :
            pg.QUIT
    pg.draw.line(screen, (0, 255, 0), 
		[mx, my], 
		[Width/2 - 20 , Height - 20], 15)
    
    pg.draw.line(screen, (0, 255, 0), 
				[mx, my], 
				[Width/2 - 20  + 20 , Height - 20], 5)
    
    pg.draw.line(screen, (0, 255, 0), 
				[mx, my], 
				[Width/2 - 20  - 20 , Height - 20], 5)
    
    pg.display.update()
