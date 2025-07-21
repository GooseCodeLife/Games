import pygame as pg
import random

pg.init()
font = pg.font.Font('freesansbold.ttf', 16)

# create a text surface object,
# on which text is drawn on it.

running = True 

#variables 
rows = 16
cols = 16
bombs = 40
buttons = [] 
mines = [0]*256

height = 20
width = 20

screen = pg.display.set_mode(((width+2)*cols +30 +40,(height+2)*rows +30 +40))

#class
pg.display.flip()
class Button () :
    def __init__ (self,x,y,bomb) : 
        self.x = x 
        self.y = y 
        self.bomb = bomb
        self.open =False
        self.nearby_mines = None 
        #self.color= (189,189,189)
    def draw(self): 
        c= (189,189,189)
        if self.open:
            c=(222,222,222)
        if self.open and self.bomb : 
            c = (202,0,0)

        pg.draw.rect(screen,c, ( self.x*(height+2) +35,self.y*(width+2)+35, height, width))
        if self.open and self.nearby_mines > 0 : 
            text = font.render(str(self.nearby_mines), True, 'blue', None)
            textRect = text.get_rect()
            textRect.center = ( self.x*(height+2) +45,self.y*(width+2)+45)
            screen.blit(text, textRect)

        

    def count_bombs(self,buttons) : 
        count = 0 

        top_left = (self.x-1,self.y-1)
        top_up = (self.x,self.y-1)
        top_right = (self.x +1,self.y-1)
        right = (self.x +1 , self. y)
        left = (self.x-1, self.y)
        bottom_left = (self.x-1, self.y +1)
        bottom_down = (self.x , self.y+1)
        bottom_right = (self.x+1 , self.y+1 )

        all_negihbours=[top_left,top_up,top_right,right,left, bottom_left, bottom_down, bottom_right]
        for n in all_negihbours:
            c= self.get_cell(buttons, n[0], n[1])
            if c !=None and c.bomb:
                count =count + 1
        self.nearby_mines = count         
    def get_cell(self,buttons,row,col) : 
        for b in buttons:
            if b.x== row and b.y == col:
                return b
    

    def is_hit (self,pos) : 
        r =  ( self.x*(height+2) +35,self.y*(width+2)+35, height, width)
        if pos[0] >= r[0] and pos[1] >= r[1] and pos[0] <= r[0]+width and pos[1] <= r[1] + height : 
            self.click()

    def click (self) :
        print('CLICKED',self.x, self.y, self.nearby_mines, self.bomb) 
        if (self.open == False) : 
            self.open = True 

my_set = set() ## 0.225
while len(my_set)<40:
    r= random.randint(0,rows*cols)
    my_set.add(r)


#create buttons
count = 0 
index=0
choice = False 
for row in range(rows): 
    for col in range(cols) :
        choice = (index in my_set) 
        
        b = Button(row,col,choice)
        buttons.append(b)
        index=index+1
        if choice == True : 
                count += 1 
        print( choice,index,count)
for b in buttons : 
    b.count_bombs(buttons)
        
        










