import pygame as pg 
import random 
import time 
screen = pg.display.set_mode((260,260))

#font = pg.font.Font('Ariel', 32)
pg.init()
pg.font.init()
font = pg.font.SysFont('Times', 20)
amount = 2
#loading image
Grey_Box = pg.image.load('Grey_Square.png').convert_alpha()
Wrong_Box = pg.image.load('Wrong_Square.png').convert_alpha()

Blue_Box = pg.image.load('Blue_Box.png').convert_alpha()

lost_text = font.render('You Lost!',True,pg.Color('white'))
win_text = font.render('You Win!',True,pg.Color('red'))

textrect = lost_text.get_rect()
textrect.center = (50,50)

#class
class Box (pg.sprite.Sprite) :
   
    def __init__ (self,x,y, isBlue):
        super().__init__() 
        self.x = x 
        self.y = y               
        self.isBlue = isBlue
        self.hide = True #At Start        
        self.discovered = False #After Hit
        
    def draw (self,screen) :
        if self.hide == True :
            screen.blit(Grey_Box,(self.x,self.y))
        else : 
            if (self.isBlue):
                screen.blit(Blue_Box,(self.x,self.y))
            else:
                if self.discovered:                   
                    screen.blit(Wrong_Box,(self.x,self.y))
                else:
                    screen.blit(Grey_Box,(self.x,self.y))

    def hit (self,mx,my) :
        if mx>=self.x  and mx <= self.x+ 30   : 
            if my >= self.y and my <= self.y + 30 : 
                self.appear()
                return True
    def appear (self) : 
        self.hide = False
        self.discovered = True 
        
    def printMe  (self) : 
        #self.hide == False
        print("printMe", self.discovered, self.isBlue, self.hide)
        print("IsBlue" , self.isBlue)
#function
class Game () :
    def __init__ (self):
        #pass 
        self.blues = 2
        self.found = 0
        self.Boxes = []
        self.blue_boxs = set() 

    def reset(self,blues):
        self.found = 0       
        del self.Boxes[:]
        self.blue_boxs = set() 
        self.create(blues)

    def lost(self):
         self.blues-=1
         self.reset(self.blues)   
    def won(self):
       self.blues+=1
       self.reset(self.blues)
    def foundBox(self):
        self.found+=1
        print("found out of" ,self.found, self.blues)

    def isWon(self):
        return self.found>= self.blues

    def displayWinMessage(self):
            print('You WIN')
            pg.draw.rect(screen, pg.Color('black'),pg.Rect(0, 0, 260, 260)  ) 
            screen.blit(win_text,textrect )
            pg.display.update()
            time.sleep(2)    
            pg.display.update()
            

    def displayLostMessage(self, screen):
        print('You Lost')
        pg.draw.rect(screen, pg.Color('black'),pg.Rect(0, 0, 260, 260)  ) 
        screen.blit(lost_text,textrect )
        pg.display.update()
        time.sleep(2)    
        pg.display.update()
            
       
    def create(self, blues):             
        self.blues=blues
        while (len(self.blue_boxs)< self.blues) : 
            self.blue_boxs.add(random.randint(0,24))
    
        print("bb",self.blue_boxs)
    
        index=0
        for row in range (5) : 
            for column in range (5) :
                index= row*5 + column
                isBlue = (index in self.blue_boxs)
                print(index, isBlue)
                box = Box(10+row*40,10+column*40, isBlue)
                box.hide = False
                box.draw(screen)            
                self.Boxes.append(box)
        pg.display.update()
        time.sleep(3)
    
        for box in self.Boxes:
            box.hide = True
            box.draw(screen)
        pg.display.update()
        print("Ready")
    def gameLoop(self):
        while True : 
            for event in pg.event.get() :
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.MOUSEBUTTONUP:
                    mx,my = pg.mouse.get_pos()
                    for box in self.Boxes :
                        if box.hit(mx,my) :
                            #box.appear()
                            box.draw(screen)
                            pg.display.update()
                            time.sleep(1)
                            if not box.isBlue:
                                box.discovered=True
                                box.draw(screen)
                                pg.display.update()
                                time.sleep(1)
                                print ("You Loose")
                                self.displayLostMessage(screen)
                                self.lost()
                            else :
                                self.foundBox()
                                box.draw(screen)
                                pg.display.update()
                                if self.isWon() : 
                                    self.displayWinMessage()      
                                    self.won()

                pg.display.update()


game=Game()
game.create(3)
game.gameLoop()