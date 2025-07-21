import turtle 

p = turtle.Turtle()
p.goto(0,0) 
for i in range(4):
    p.forward(10)
    p.left(90)

def square (x,y) : 
    p.goto(x,y)
    for i in range(4):
        p.forward(20)
        p.left(90) 

def anysquare (f):
    for i in range(4): 
        p.forward(f)
        p.left(90) 