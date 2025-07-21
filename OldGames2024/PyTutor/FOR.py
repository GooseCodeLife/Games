#multiplication table of the number the user 
x = int(input('Input number for multiplication number '))
for i in range (1,11) :
    print (x,'*',i,'=',x*i)

#if even print square of a number if odd print cube of a number from 1 to 20
for i in range (1,21) :
    if i%2 == 0 : 
        print (i,i*i)
    else :
        print (i,i*i*i)

#print all numbers divisible by 2 or 7 but not by both
for i in range (1,101) :
    if i%2 == 0 and i%7 == 0 :
        continue
    if i%2 == 0 or i%7 == 0 :
        print (i,end = ' ')