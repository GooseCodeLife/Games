#alphebatize words
x = 'computer'#xylophone 
a = [x[0]]
#ord

y = int(ord(x[0]))
for i in range (1, len(x)) :
    
    if y < ord(x[i]):
        print(ord(x[i]))
        a.append(x[i])
        y = ord(x[i])
        
l = 'r'
for i in range (len(a)) :
    if ord(l) > ord(a[i]) : 
        continue
    a.insert(i,l)
    break
print(a)                    