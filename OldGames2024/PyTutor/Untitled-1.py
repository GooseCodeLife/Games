#armstrong numbers for any number
x = int(input('Enter a number '))
while x != 0 : 
    print(x % 10)
    x = x // 10 

#Example what LEN does
x = (input('Enter any number'))
l = len(x)
x = int(x)
print(x, l)

#armstrong numbers for 3 digit numbers
x = int(input('Enter a 3 digit number '))
hundred_place = x//100 
ones_place = x % 10 
tens_place = x // 10 % 10 
y = hundred_place**3  
z = ones_place**3 
d = tens_place**3 
if y+z+d == x : 
    print('This is a armstrong number')
else : 
    print('This is not an armstrong number')

#3 digit number and add them
x = int(input('Input a 3 digit number '))
print(x//100 + x % 10 + x // 10 % 10 ) 

''''
x // 100 # hundreds 
x % 10 # ones 
x // 10 % 10 # TENS
'''

#find perfect numbers
total = 0
x = int(input('Input Number to identify if perfect or not '))
for i in range (1,x) :
    if x%i == 0 :
        total = total + i
if total == x :
    print('This number', x, 'is a perfect number')
else :
    print('This number', x, 'is not a perfect number')

#find the factors of numbers 
x = int(input('Input a number to factor '))
for i in range (1,x+1) : 
    if x%i == 0 :
        print (i)
    

#multiply 5 different numbers and show their product 
total = 1
y = ''
for i in range (5): 
    x = int(input('Input number '))
    total = total * x    
    y = y + "*" + str(x) 
print (y, '=', total)



#ask 5 numbers from user and show their sum
total = 0
y = ''
for i in range (5): 
    x = int(input('Please input number '))
    total = total + x 
    y = y + '+' + str(x)
print (y, "=", total)