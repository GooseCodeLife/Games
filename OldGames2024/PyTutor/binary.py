def convertdecimaltobinary (x) :
    ans = ''
    i = 0
    while x > 0  :
        ans = str(x%2) + ans
        x = x//2 
    
    return ans

def binarytodecimal (x):
    ans = 0
    pos = 0
    for i in range (len(x)-1,-1,-1) :
        if int(x[i]) == 1 : 
            ans = ans + 2**pos
        pos = pos+1
    return ans

#binarytodecimal(str(101))
#convertdecimaltobinary(12)0

#  100101010101010 
#   
def wordtobinary(x) : 
    ans = ''
    for i in x :     
                                                                        
        a = ord(i)
        ans = ans + convertdecimaltobinary(a) + ''
    return ans


#   10010011000001101100110100111010111100101100000111000011110011110100110100011011111101110 
#   1111010         
#get a string of anything abc
#convert it into binary "1111101111100010101000"   sentence witgh every
#from that binary find the maximum number

'''
sol = 0
p = 2
a = 0
ans = 'kavya'
while a < 5 :
    if sol == 'vy' : 
        print(sol)
        break
    sol = ans[a:a+p]
    a = a + 1
'''
# Answer!!!
item = 'the great undertaking'
found = False
i = 0
while found == False :
    y = str(wordtobinary(item)) 
    s = str(convertdecimaltobinary(i))
    if s in y :
        i = i + 1 
    else : 
        found = True
        print(i) 
















