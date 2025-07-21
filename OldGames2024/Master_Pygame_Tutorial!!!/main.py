import pygame as pg 
from random import randint
from os.path import join 
#general set up
pg.init() 
screen = pg.display.set_mode((1280,720)) 
running = True
clock = pg.time.Clock()
#plain surface
surf = pg.Surface((100,200))
surf.fill('orange')
x = 100 
pg.display.set_caption('Space Shooter')
#importing images
#loading images
laser_surf = pg.image.load(join('5games-main','spaceshooter','images','laser.png')).convert_alpha()
meteor_surf = pg.image.load(join('5games-main','spaceshooter','images','meteor.png')).convert_alpha()
player_surf = pg.image.load(join('5games-main','spaceshooter','images','player.png')).convert_alpha()
star_surf = pg.image.load(join('5games-main','spaceshooter','images','star.png')).convert_alpha()
#rects
player_rect = player_surf.get_frect(center = (1280/2,720/2))
player_direction = 1
meteor_rect = meteor_surf.get_frect(center = (1280/2,720/2))
laser_rect = laser_surf.get_frect(bottomleft = (20,700))
star_positions = [(randint(0,1280), randint(0,720)) for i in range(20)]
pg.display.update()
while running  : 
    clock.tick(1)
    for event in pg.event.get() :
        if event.type == pg.QUIT: 
            running = False 

    #draw the game 
    screen.fill('darkgray')
    #star
    for pos in star_positions :
        screen.blit(star_surf,pos)
    
    #other drawings
    screen.blit(meteor_surf, meteor_rect)
    screen.blit(laser_surf,laser_rect)

    #player movement
    player_rect.x += player_direction *0.4
    if player_rect.right > 1280 or player_rect.left < 0 :
        player_rect.left += 0.2
    screen.blit(player_surf, player_rect.topleft)
    pg.display.update() 

pg.quit()