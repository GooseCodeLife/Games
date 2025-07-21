#Tic tac toe 
import turtle 
s = turtle.Screen()
m = turtle.Turtle() 
p = turtle.Turtle()
p.color('yellow')
p.penup()
p.hideturtle()
player = 'x'
s.bgcolor('black')
m.color('white')
m.shape('turtle') 
m.hideturtle()
def tictac (x1,y1,x2,y2) :
    m.penup()
    m.goto(x1,y1) 
    m.pendown()
    m.goto(x2,y2)

tictac(-200,100,100,100)
tictac(-200,0,100,0)
tictac(-100,200,-100,-100)
tictac(0,200,-0,-100)
def tap (x,y) : 
    if x > -200 and x < -100 and y > 100 and y < 200 : 
        p.goto(-150,150)
        p.write(player,font=('Arial',30))
    elif x > -100 and x < 0 and y > 100 and y < 200 : 
        p.goto(-50,150)
        p.write(player,font=('Arial',30))
    elif x < 100 and x > 0 and y < 200 and y > 100 : 
        p.goto(50,150)
        p.write(player,font=('Arial',30))
    elif x > -200 and x < -100 and y < 100 and y > 0 :
        p.goto(-150,50)
        p.write(player,font=('Arial',30))
    elif x > -100 and x < 0 and y > 100 and y < 200 : 
        p.goto()
s.onscreenclick(tap)
input()
