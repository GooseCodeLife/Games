#pig challenge you start out with a die
import random
n=0
f = 0
dice = [1,2,3,4,5,6]
k = False
while k== False : 
    x = input('Do you want to roll? ')
    if x == 'yes' :
        ans = random.choice(dice)
        if n != 100 :
            if n > 100 :
                print('You Won')
                k == True
                exit()
            else :
                if ans == 1 : 
                    print('You lost everything, you PIG')
                    f = 0
                else :
                    f = f + ans
                    print(f)
    elif x == 'no':
        n = n + f
        f = 0
    else:
        print(f'Your total score so far is!{f}')









