#very basic flappybird
import pygame
import random
pygame.init()
Width = 550
Height = 600
screen = pygame.display.set_mode((Width,Height))
Velocity = 5
x = 10
y = 95
FPS = 5
clock = pygame.time.Clock()
import time
pipe_x = 300
#define variables
ground_scroll = 0
ground_speed = 4
#start x and end x and y and 
# create a surface object, image is drawn on it.
img = pygame.image.load("flappy.png").convert_alpha()
pipe_up = pygame.image.load("pipe_up.png").convert_alpha()
img1 = pipe_up.copy()
pipe_down = pygame.transform.flip(img1,False,True)

background = pygame.image.load("background1.png").convert_alpha()
ground = pygame.image.load("ground.jpg").convert_alpha()

y_gap= [random.randint(300,400),random.randint(300,400),random.randint(300,400)] 
# paint screen one time
pygame.display.flip()
status = True
while True : 
    screen.fill((0,0,0))
    y = y + 3 + Velocity
    Velocity = Velocity +1 
    #for eventss  
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
        #commands
        if event.type == pygame.MOUSEBUTTONUP:
            y = y - 55
            Velocity=1
    screen.blit(background, (0,0))
    screen.blit(img, (x, y))

    #screen.blit(pipe,(200,340))
    for i in range(len(y_gap)) :
        y_ps = y_gap[i]
        pipe_up_y =y_ps-430
        pipe_down_y =y_ps
        pipe_start_x = pipe_x + i*250
        pipe_end_x = pipe_start_x + 100
        pipe_mid = (pipe_start_x + pipe_end_x)/2
        flappy_x = x
        flappy_endx = x + 89
        flappy_y = y
        flappy_endy = y + 69
        if flappy_endx > pipe_start_x and flappy_x < pipe_end_x: 
            print('YOU ARE NEAR PIPE NOW CHECK Y')
            # if bird is hitting the up pipe
            if flappy_y < (pipe_up_y +217) or flappy_endy > pipe_down_y: 
                x = 800
                print('You Lost you absolute FOOL')

        screen.blit(pipe_up,(pipe_start_x,pipe_up_y))
        screen.blit(pipe_down,(pipe_start_x,pipe_down_y))
    for i in range(1):
        pipe_x = pipe_x - 7
    print("pipe_x", pipe_x)
    if (pipe_x<=0):
        print("newpi[]")
        y_gap.append(random.randint(300,400))




    #ground
    screen.blit(ground,(ground_scroll,570))
    ground_scroll -= ground_speed
    if abs(ground_scroll) > 35 :
        ground_scroll = 0
    pygame.display.update()
    clock.tick(FPS)









