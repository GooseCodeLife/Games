#string logic 
#Sentence = 'I love my rabbit who is named ojo'
#word = 'loved'
#n = len(word)
#for i in range(len(Sentence)) :
#    if Sentence[i:i+n] == word :
#        print(Sentence[i:i+n])



#word = 'yes the Earth is proven to not be flat'
#for i in range (len(word)-1,-1,-1): 
#    print(word[i],end = '')

paladrome = True
s = input('Enter a paladrome ') 
for i in range (len(s)//2) :  
    f = s[i]
    l = s [len(s)-1-i]
    if f != l :
        paladrome = False 
        break 
if paladrome == False : 
    print('this is not a paladrome') 
else : 
    print('This is a paladrome')

#print(f,l) 

    
