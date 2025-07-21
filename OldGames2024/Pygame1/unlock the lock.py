#unlock the lock
import turtle 
import random
import sys
s = turtle.Screen()



point = turtle.Turtle() 
point.shape('circle') 
point.color('yellow')
point.goto(0,175)




p = turtle.Turtle()
p.shape('square')
p.shapesize(1.3, 0.7, 0.1)
p.speed(50)
p.color ('green')
p.penup() 
p.goto(0,175)
p.showturtle()

a=0
n=0
score=0
point.speed(1000)
def randommove () : 
    global n
    n = random.randint(1,36*2)
    point.hideturtle() 
    point.penup()
    for i in range(n): 
        point.right(5)
        point.forward(10) 
    point.showturtle() 

randommove()


def moveright () :
    global a
    a=1
    for i in range(360) : 
        if not gameover:
            p.right(1)
            p.forward(2)
        
    
def moveleft () : 
    global a
    a = 2
    for i in range(360) :
        if not gameover:
            p.left(1) 
            p.forward(-2)

start =False
gameover = False
def hit () :
    global score
    global gameover
    print("Hit")
    print(p.distance(point))
    if p.distance(point) < 25 :
        print(score) 
        score = score + 1
        randommove()
        if a==2:
            moveright()
        else:
            moveleft()
    else : 
        print("Game Over")
        gameover = True
        sys.exit()
def moveDifferentDirection():
    #if moving:
    #    return
    global start 
    global a 
    global score
    print(score)
    if gameover:
        return
    if start == False : 
        start = True 
        moveright()
        
        return  
    if hit():
        pass
    
        
s.onkey(moveDifferentDirection, 'space')



s.listen()





input()
