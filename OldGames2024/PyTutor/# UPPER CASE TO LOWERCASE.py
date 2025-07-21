# UPPER CASE TO LOWERCASE

s = input('Enter a letter uppercase or lowercase: ')
for i in range (len(s)) :
    if ord(s[i]) >= 65 and ord(s[i]) <= 90 : 
        print(chr(ord(s[i])+32))
    elif ord(s[i]) >= 97 and ord(s[i]) <= 122:
        print(chr(ord(s[i])-32))
