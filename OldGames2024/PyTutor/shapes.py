import turtle
t = turtle.Turtle()
t.shape('turtle')
t.pensize(3)
t.color('purple')
x = int(input('Enter the number of sides for the shape: '))
while x != 0 :
    for i in range(x):
        t.forward(1)
        t.left(360/x)
    x = int(input('Enter 0 to stop: '))
input()