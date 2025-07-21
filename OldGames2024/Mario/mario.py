import pygame as pg

screen = pg.display.set_mode((400,400))
#class Toad(Sprite.sprite)
clock = pg.time.Clock()
FPS = 30
''''
Toad1 = pg.image.load('NewToad.png').convert_alpha()
Toad2 = pg.image.load('Toad-2.png').convert_alpha()
Toad3 = pg.image.load('Toad-3.png').convert_alpha()
Toad4 = pg.image.load('Toad-4.png').convert_alpha()
'''
#pg.image.load("flappy.png").convert_alpha()
imgs=[]
for num in range(1,5):
        img = pg.image.load(f'Toad-{num}.png').convert_alpha()
        imgs.append(img)

image = imgs[0]

screen.fill((0,0,0))

angle = 0
x=20
while True:

    rotated_image = pg.transform.rotate(image, angle)
    angle += 8
    x +=1.5
    screen.fill((0,0,0))
    clock.tick(FPS)
    screen.blit(rotated_image, (x,50))
    pg.display.update() 
    #pg.display.flip()

"""
while True :    
    screen.fill((0,0,0))
    for i in range(4):
        index = i 
        screen.fill((0,0,0))
        screen.blit(imgs[i],(50,50))
        clock.tick(FPS)
        pg.display.update() 

    '''
        screen.blit(Toad2,(50,50))
        screen.blit(Toad3,(50,50))
        screen.blit(Toad4,(50,50))
    '''
"""    