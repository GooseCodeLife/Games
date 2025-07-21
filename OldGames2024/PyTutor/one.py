#import random 
#r1 = random.randint(5,34)
#//print(r1)

# you have to put this every single time you use the "random command"
import random 
possible_choices = ['rock', 'paper', 'scissor']
user_choice = input("enter a choice (rock, paper, or scissors):  \t")
computer_choice = random.choice(possible_choices)
#/t is tab
#/n is next slide
print('user choice :' + user_choice)
print(f'you choice : {user_choice} the computer chose {computer_choice}')

# if user_choice == computer_choice:
#     print('its a draw')
# elif user_choice == 'rock' :
#     if computer_choice == 'scissor':
#         print('YOU WON')
#     else :
#         print('You lose')
# elif user_choice == ('paper')
