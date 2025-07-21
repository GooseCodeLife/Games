



#GUESS THE NUMBER
import random 
secret = random.randint(1,10)
win = False
for i in range(3) :
    x = int(input('Enter a number between 1-10 ')) 
    if x == secret :
        print ('You got the number!')
        win = True 
        break
    elif x >= secret : 
        print ('Your number is greater than the secret number')
    else :
        print ('your number is less than the secret number')
if win == False :
    print ('you lost the game')


#what ride can you go on depending on your age
x = int(input('What is your age? ')) 

if x <= 10 :
    print ('you are too young to go on either rides')
elif x >= 10 and x <= 15 :
    print ('you can only go on ride A')
elif x >= 15 and x <= 18 :
    print ('you can only go to ride B')
else :
    print ('you are too old ')


#what type of triangle is this based of length
x = int(input('first length of triangle '))
y = int(input('second length of triangle '))
z = int(input('third length triangle '))

if x == y and y == z and z == x : 
    print ('equilateral')
elif x == y or z == y or z == x : 
    print ('isosceles')
else :
    print ('scalene')

#numbers how they work fudge
first =2
second = 3
third = first*second
second = third - first
first = first + second + third
third = second * first
print('{} {} {} {} '.format(third, second, first ,third) )


#numbers
x = 10
x = x + x
x = x - 5
x = (x*5)/5 + 10
print("The value of x:",x)




#even or odd
x = int(input('Enter a number '))
if x%2 == 0:
    print ('even')
else: 
    print ('odd') 

#numbers
x = 10
x = x + x
x = x - 5
x = (x*5)/5 + 10
print("The value of x:",x)