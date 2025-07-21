#hangman
import random
'''
steps:  
1. make  it so like it gives you a random word thats like 5 letters long
2. make it that way the person can like guess the letter
3. make it that way the person can find out if they're wrong or right
4. make it that way the person can find out how many moves they have left until hangman dies
5. show them the letters that are completed like if you get a then it would be A__a__
'''
stickmen = [
"\
|------\n\
|    O\n\
| ---|---\n\
|   / \\ \n\
|  /   \\ \n\
|_____",

"\
|------\n\
|    O \n\
| ---|---\n\
|\n\
|\n\
|_____",

"\
|------\n\
|    O\n\
|\n\
|\n\
|\n\
|_____",

"\
|------\n\
|\n\
|\n\
|\n\
|\n\
|_____",

"\
|\n\
|\n\
|\n\
|\n\
|_____",

"\n\n\n\n______",

"\n\n\n\n\n",
]
count = 7
word = ['smile', 'fight', 'robot', 'mouse', 'paper', 'video', 'upper'] 
secret = (random.choice(word))
usedletters = []
    
        
while True :                                   
    guess  = (input('Enter a letter for a 5 letter word: '))
    display = ''
    if guess in usedletters:
         print('This letter is already guessed please state another letter')
         continue
    else :
        count = count - 1

    for i in secret :
        if count == 0 :
            print('YOU LOST')
            exit()
        elif i in usedletters and i in secret : 
            display += i 
        elif i == guess : 
            display = display + guess
        else : 
            display += '_'
    usedletters.append(guess)
    print('Used Letters: ', usedletters)
    print(display)

    
    if display == secret : 
        print('YOU SAVED HANGMAN')
        exit()


    if guess in secret :
        
        print('found')
    else :
        print('not found')
        print(stickmen[count]) 




    