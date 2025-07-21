#ATM
import random
x = str(input('Please input your name to access your account details: '))
balance = random.randint(1,10000)
y = 0
while y != 4 :
    if x == 'Kavya' : 
        y = int(input('What would you like 1 to withdraw 2 to deposit 3 to check balance and 4 to quit: '))
        if y == 1: 
            print(balance)
            withdraw = int(input('How much would you like to withdraw: '))
            if withdraw >= balance : 
                print('Your withdraw amount is over your balance please pick another')
                withdraw = int(input('How much would you like to withdraw: '))
                print(balance-withdraw)
                balance = balance-withdraw
            else :
                print(balance-withdraw)
                balance = balance-withdraw
        elif y == 2 : 
            print(balance)
            deposit = int(input('How much would you like to deposit: '))
            print(balance+deposit)
            balance = balance + deposit
        elif y == 3 : 
            print('Your balance is currently', balance)
        elif y == 4: 
            print('Thank you for using the ATM the program has ended hope you had a good experience')
        

else : 
    print('Invalid Name')
