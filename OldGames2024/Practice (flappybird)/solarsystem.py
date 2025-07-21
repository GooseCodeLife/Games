import pygame as pg
pg.init() 
Width = 500
Height = 500
screen = pg.display.set_mode((Width,Height))

class Planet :
    def __init__ (self, name, color,radius) :
        self.name = name 
        self.color = color 
        self.radius = radius 
    def func2 (a) : 
        print('My name is' + a.name)

Earth = Planet('Earth','red',12)

'''
while True :
    for event in pg.event.get() : 
        if event.type == pg.QUIT :
            pg.QUIT 
    screen.fill((0,0,0))


    
    pg.display.update()
    '''