x = int(input('Enter a number '))

prime_number = True  
for i in range (2,x):
    if x%i ==0:
        prime_number =  False
        break

        
if prime_number == True : 
    print('IS a prime number') 
else :
    print('not a prime')





