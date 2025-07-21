'''
n = 0

for row in range(5): 
    print(' ')
    for column in range(4): 
        print('*', end = '')



for row in range(4) :
    print()
    for column in range(4): 
        if row == column : 
            print('*', end = ' ') 
        else : 
            print(' ',end = ' ')


for row in range(3) : 
    for column in range(4): 
        print(4* row + column + 1 , end = ' ' )
    print()
'''
r = 4
for row in range(4):
    for i in range(r-1):
        print(' ', end = ' ')
    r = r - 1 
    for column in range(2*row+1): 
        print('*', end = ' ')
    print()




