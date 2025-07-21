import pygame as pg
import math 
from math import *
clock = pg.time.Clock()
screen = pg.display.set_mode((700,700))
class Planet :
    def __init__ (self, name, color,radius,x,y,angle,dist,angle_amount,height,width) :
        self.name = name 
        self.color = color 
        self.radius = radius 
        self.x = x
        self.y = y
        self.angle = 0
        self.dist = dist
        self.angle_amount = angle_amount
        self.height = height
        self.width = width
    def move_planet (self) : 
        self.x =  self.dist*cos(self.angle)
        self.y =   self.dist*sin(self.angle)
        self.angle = self.angle + self.angle_amount
        pg.draw.ellipse(screen, self.color, pg.Rect(200+self.x,200+self.y,self.height,self.width))

Mercury = Planet('mercury','brown',12,50,50,0.1,40,0.05,20,20)
Venus = Planet('Venus','red',12,50,50,0.2,80,0.03,40,30)
Earth = Planet('Earth','green',12,50,50,0.3,100,0.01,40,40)
Mars = Planet('Mars','red',12,50,50,0.4,150,0.007,50,50)
Jupiter = Planet('Jupiter','yellow',12,50,50,0.5,180,0.02,40,40)
Saturn = Planet('Saturn','brown',12,50,50,0.6,230,0.018,40,40)
Uranus = Planet('Uranus','red',12,50,50,0.7,250,0.016,50,50)
Neptune = Planet('Neptune','blue',12,50,50,0.8,280,0.005,60,60)
Moon = Planet('Moon','gray',12,20,20,0.1,130,0.02,10,10)
planets = [Mercury,Venus,Earth,Mars,Jupiter,Saturn, Uranus, Neptune,Moon]

while True:
    for event in pg.event.get() : 
        if event.type == pg.QUIT :
            pg.QUIT
    
    screen.fill((0,0,0))
    for i in planets : 
        Moon.x = Earth.x
        Moon.y = Earth.y
        i.move_planet()

    clock.tick(100)
    pg.display.update()