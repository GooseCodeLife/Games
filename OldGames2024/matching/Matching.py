#matching
import pygame as pg 
import random
screen = pg.display.set_mode((500,600))
pg.init()
#loading all the images
back = pg.image.load('card.png').convert_alpha() 
Lamp_Grass = pg.image.load('Lamp_Grass.png').convert_alpha()
flower = pg.image.load('flower.jpg').convert_alpha()
Qingxin = pg.image.load('Qingxin.jpg').convert_alpha()
Purple = pg.image.load('Purple.png').convert_alpha()
Silk_Flower = pg.image.load('silkf.jpg').convert_alpha()
Snap_Dragon = pg.image.load('Snap_Dragon.png').convert_alpha()
Witch_Fire = pg.image.load('Witch_Fire.jpg').convert_alpha()
Wonderous_Flower = pg.image.load('Wonderous_Flower.jpg').convert_alpha()
#lists
Cards = []
Flower = [Lamp_Grass,flower,Qingxin,Purple,Silk_Flower,Snap_Dragon,
Witch_Fire,Wonderous_Flower,Lamp_Grass,flower,Qingxin,Purple,Silk_Flower,
Snap_Dragon,Witch_Fire,Wonderous_Flower]
#class Card
class Card (pg.sprite.Sprite): 
    def __init__(self, back_img, front_img,x, y): 
        super().__init__() 
        self.back_img = back_img
        self.front_img = front_img
        self.x = x
        self.y = y 
        self.hide = True
    def draw (self,screen) :
        if self.hide == True :           
            screen.blit(self.back_img,(self.x,self.y))
        else: 
            pg.draw.rect(screen, pg.Color('black'),pg.Rect(self.x, self.y, 78, 108)  )       
            screen.blit(self.front_img,(self.x,self.y))
    def hit (self,mx,my) :
        if mx>=self.x  and mx <= self.x+ 78   : 
            if my >= self.y and my <= self.y + 108 : 
                return True
    def appear (self) : 
        print('Self.hide == False')
        self.hide = False 
    def matching (self, anotherCard ) : 
        if anotherCard.front_img == self.front_img :
            return True
    def appear (self) :
        self.hide == False
    def flip (self) :
        self.hide = True

#draws cards
for row in range(4):    
    for column in range(4):  
        item = random.choice(Flower) 
        k = item     
        card = Card(back,item,10+row*130 + 10 ,10+column*130+10)
        card.draw(screen)
        Flower.remove(item)
        Cards.append(card)

#print(random.choice(foo))
pg.display.update()
lastCard = None
score =0
while True :
    for event in pg.event.get() :
        if event.type == pg.QUIT:
            pg.quit()
        #commands
        if event.type == pg.MOUSEBUTTONUP:
            (mx,my) = pg.mouse.get_pos()
            print(mx,my)

            for card in Cards : 
                #card hit
                if card.hit(mx,my) :
                    print('I clicked the card', card.hide)
                    card.appear() 
                    print('I clicked the card', card.hide)
                    card.draw(screen)
                    if lastCard == None:
                        lastCard = card
                    else:
                        if lastCard.matching(card) :
                            print ('matching', score)
                            score = score + 1
                            lastCard = None
                            if score >= 8 : 
                                print('You WIN')
                        else :
                            print ('not matching')
                            lastCard.flip()
                            card.flip()
                            card.draw(screen)
                            lastCard.draw(screen)
                            lastCard = None
    pg.display.update()