#very basic flappybird
import pygame
import random
pygame.init()
Width = 550
Height = 600
screen = pygame.display.set_mode((Width,Height))
Velocity = 0
x = 10
y = 95
FPS = 5
clock = pygame.time.Clock()
pipe_x = 200
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
# Using blit to copy content from one surface to other
#scrn.blit(imp, (0, 0))
#my worst enemy = class

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
            y = y - 50
            Velocity=1
    screen.blit(background, (0,0))
    screen.blit(img, (x, y))

    #screen.blit(pipe,(200,340))
    for i in range(3) :
        y_ps = y_gap[i]
        pipe_up_y =y_ps-430
        pipe_down_y =y_ps
        pipe_start_x = pipe_x + i*250
        pipe_end_x = pipe_start_x + 100
        
        pipe_mid = (pipe_start_x + pipe_end_x)/2
           
    
        screen.blit(pipe_up,(pipe_start_x,pipe_up_y))
        screen.blit(pipe_down,(pipe_start_x,pipe_down_y))
        
        bird_start_x = x
        bird_end_x = bird_start_x + 90
        bird_mid = (bird_end_x+bird_start_x)/2

        x_dis = abs(pipe_mid-bird_mid)

        

        if (x_dis)<60:
            print ("pipe x is touching bird" , x_dis,y)
            
            bird_start_y = y
            bird_end_y = bird_start_y + 90
            bird_mid_y = (bird_end_y+bird_start_y)/2

            gap_end = y_ps 
            gap_start = gap_end - 90  

            gap_mid = (gap_end + gap_start)/2

            y_dis =   abs(gap_mid-bird_mid_y)

            if (y_dis) >100 : 
                print ("collide : pipe x and y is touching bird" , x_dis, y_dis)
            else:
                print ("Passing in safe distance from gap", y_dis)


    


      
    pipe_x = pipe_x - 3
    
    #ground
    screen.blit(ground,(ground_scroll,570))
    ground_scroll -= ground_speed
    if abs(ground_scroll) > 35 :
        ground_scroll = 0
    pygame.display.update()
    clock.tick(FPS)









