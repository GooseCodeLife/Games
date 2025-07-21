import pygame
from pygame.locals import * 

pygame.init()

WIDTH = 1000
HEIGHT = 1000 
screen = pygame.display.set_mode((WIDTH,HEIGHT))

run = True
while run == True : 
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : 
            run = False 






