#TAG GAME really fun liked
import turtle 
import random 
s = turtle.Screen()
def Turtlee (c) :
    t = turtle.Turtle()
    t.shape('turtle')
    t.color(c)
    t.penup()
    t.goto(random.randint(-200,200),random.randint(-200,200))    
    t.seth(random.randint(-180,180))
    return t 

p = Turtlee('indigo') 
g = Turtlee('dark green')
pi = Turtlee('dark green') 
o = Turtlee('dark green')
y = Turtlee('dark green')
z = Turtlee('dark green')
r = Turtlee('red') 
red2 = Turtlee('orange')
player2 = Turtlee('black')
score = Turtlee('black') 
score.hideturtle()
score.goto(190,190)
    
gt = [g,pi,o,y,z]
def moveleft() : 
    y = p.xcor()
    y = y - 10 
    p.setx(y) 

def moveright() : 
    y = p.xcor() 
    y = y + 10 
    p.setx(y)

def movedown () : 
    y = p.ycor()
    y = y - 10 
    p.sety(y) 

def moveup ():
    y = p.ycor()
    y = y + 10
    p.sety(y)

#PLAYER2
def moveleft2(): 
    y = player2.xcor()
    y = y - 10 
    player2.setx(y)

def moveright2 (): 
    y = player2.xcor()
    y = y + 10 
    player2.setx(y)

def movedown2 (): 
    y = player2.ycor()
    y = y - 10 
    player2.sety(y)

def moveup2 (): 
    y = player2.ycor()
    y = y + 10 
    player2.sety(y)

s.listen()
#Player 2
s.onkey(moveup2, 'w')
s.onkey(movedown2, 's')
s.onkey(moveright2, 'd') 
s.onkey(moveleft2, 'a')
#Player1
s.onkey(moveup,'Up')
s.onkey(movedown,'Down')
s.onkey(moveright, 'Right')
s.onkey(moveleft, 'Left')

y = 0
def follow1():
    y = 0
    r.forward(1)
    r.seth(r.towards(p)) 
    if r.distance(p) < 10 : 
        score.clear()
        score.write('one Lose')
        p.hideturtle()
        r.hideturtle()
        return 
    for i in gt : 
        i.forward(1) 
        if i.distance(p) < 10 : 
            i.hideturtle() 
            gt.remove(i)
            y = y + 1
            score.clear()
            score.write('one score'+str(y))
            if y == 5 : 
                score.write('one Won')
y1 = 0
def follow2 () : 
    y1 = 0
    red2.forward(1) 
    red2.seth(red2.towards(player2))
    if red2.distance(player2) < 10 : 
        score.clear()
        score.write('player 2 Lose')
        player2.hideturtle()
        return 
    for i in gt : 
        i.forward(1) 
        if i.distance(player2) < 10 : 
            i.hideturtle() 
            gt.remove(i) 
            y1 = y1 + 1
            score.clear()
            score.write('player 2 score'+str(y1))
            if y1 == 5 : 
                score.write('player 2 Won')
while True:
    follow1()
    follow2()

input()