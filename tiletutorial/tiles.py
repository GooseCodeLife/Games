import pygame as pg 
screen = pg.display.set_mode((500,500))




#variables
tileHeight= 30
tileWidth = 30 
tileImg = {0 : 'blank.jpg' , 1 : 'grass.jpg' , 2 : 'ground.jpg', 3 : 'plant.jpg', 4 : 'character.jpg'}
loadedImg = {}

for k, v in tileImg.items():    
    n=tileImg[k]
    img = pg.image.load(n).convert()
    loadedImg[k]=img
    

pg.init() 
tileMap= [ [1,3,1,1,1],[1,2,2,2,1],[1,2,2,2,1],[1,1,1,1,3],[1,1,1,3,1] ]
running = True 
rows = 5
cols = 5 
screen = pg.display.set_mode((500,500))

#functions
def draw_tiles () : 
    for i in range(rows):
        for j in range(cols) : 
            tile = tileMap[i][j]
            img = loadedImg[tile]          
            screen.blit(img, (i*30,j*30))


for i in range(10000):
    draw_tiles()
    pg.display.flip()


#loop
"""
while running : 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    draw_tiles()
    pg.display.flip()
pg.quit()
"""


#i want a character that can move around 
# I want a character to be able to place, water, and pick up plants (3 types) 