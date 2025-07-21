#sheriff 
import turtle
p = turtle.Turtle()
p2 = turtle.Turtle() 
b1 = turtle.Turtle()
b2 = turtle.Turtle()
p.shape('turtle')
p2.shape('turtle')
b1.shape('circle')
b2.shape('circle')
b1.hideturtle()
b1.color('red') 
b2.color('black')
b1.penup()
b2.penup()
b2.hideturtle()
b1.hideturtle()
p.penup()
p2.penup()
p.setx(200)
p2.setx(-200)
p.right(180)

p.color('violet')
p2.color('indigo')
s = turtle.Screen()


def movedown () :
    y = p.ycor()
    y = y - 10 
    p.sety(y) 


def moveup ():
    y = p.ycor()
    y = y + 10
    p.sety(y)
    
#PLAYER2

def movedown2 (): 
    y = p2.ycor()
    y = y - 10 
    p2.sety(y)

def moveup2 (): 
    y = p2.ycor()
    y = y + 10 
    p2.sety(y)

b1firing = False

def shoot1 (): 
    global b1firing
    if b1firing:
        return
    b1firing = True
    b1.setx(200)
    y = p.ycor()
    b1.sety(y)
    b1.showturtle()
    for i in range(4):
        b1.forward(-100)

    b1.forward(-100)
    
    b1firing = False
    b1.hideturtle()
    pass

def shoot2 (): 
    b2.showturtle()
    pass

s.listen()
#Player 2
s.onkey(moveup2, 'w')
s.onkey(movedown2, 's')
s.onkey(shoot1, 'Left')
#Player1
s.onkey(moveup,'Up')
s.onkey(movedown,'Down')
s.onkey(shoot2, 'd')


input()