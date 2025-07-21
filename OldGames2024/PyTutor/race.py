import turtle  
import random 
f = turtle.Turtle()
t = turtle.Turtle()
p = turtle.Turtle()
f.shape('turtle')
f.color('green')
f.penup()
f.goto(285,150)
f.pendown()
f.right(90)
f.forward(250)

t.shape('turtle')
t.color('purple')

p.shape('turtle')
p.color('orange')

t.penup()
t.goto(-300,100)
p.penup()
p.goto(-300,-100)
while t.xcor() <= 290 and p.xcor() <= 290 : 
    t.forward(random.randint(1,10))
    p.forward(random.randint(1,10))
if t.xcor() >= 285: 
    t.goto(0,0)
    t.write('Purple is the winner')
else : 
    p.goto(0,0)
    p.write('Orange is the winner')
input()