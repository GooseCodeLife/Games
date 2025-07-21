#list challenges
import random 
'''
numberlist = []

for i in range (10): 
    x = random.randint(1,10000)
    numberlist.append(x)
    
print(numberlist)
#prints specific numbers according to index
print(numberlist[1:5])

x = 'i like python'
print(x[7:13])
'''
#we first have a really big number
#we get the first number and check if the second is bigger then the first
#if the second is bigger then the first you add it to the list
#if not then you get the next number and join it with the first
#then compare if its still not big enough get the next one
# if it is then continue on to the next number 
#repeat the process until all numbers are gone or one remaining
#which u discard

#variables
answer = []
number = '121454'#str(random.randint(10000000,20000000))
#loop
v=2
answer.append(number[0])
for i in range(len(number)-1):
    if number[i] < number[i+1] :
        answer.append(number[i+1])
    else : 
        v = v+1
        if int(number[i + 1: i + v+1]) > int(number[i:i+v-1]): # int CONVERT to int
            answer.append(number[i+1:i+v])
            i=i+v
             

print(answer)
print(number)

