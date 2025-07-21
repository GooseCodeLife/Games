#example how to make this upside down?
'''
def triangle(n):
    k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k -= 1
        for j in range(0, i+1):
            print("* ", end='')
        print()

# Driver code
triangle(5)
'''

def equilateraltriangle(n) : 
    m = n - 1
    for i in range(0,n):
        for j in range(0,m):
            print(end=" ")
        m -= 1
        for j in range(0, i+1) :
            print("* ", end='')
        print()                                          

equilateraltriangle(5)
