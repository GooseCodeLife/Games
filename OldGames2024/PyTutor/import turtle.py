import turtle 
def rectangle(l,w): 
    for i in range (2):
        t.forward(l)
        t.left(90)
        t.forward(w)
        t.left(90)
t = turtle.Turtle()
t.shape('turtle') 
t.color('purple') 
rectangle(100,60)
t.penup()
t.goto(10,35)
t.pendown()
rectangle(20,10)
t.penup()
t.goto(70,35)
t.pendown() 
rectangle(20,10)
t.penup()
t.goto(15,10)
t.pendown()
rectangle(70,10)
for i in range(7):   
    for i in range (4):
       t.forward(10)
       t.left(90) 
    t.forward(10)
    
input()