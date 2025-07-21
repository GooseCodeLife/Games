#cardgame


cards = ['7H', '3S' , '3D' ,'3C','2D','2H',]
 #input('Enter a card: 7H ')
player_letter = cards[0][1] #H
player_number = int(cards[0][0]) #
found = False
c= '10'
d = '10'

possible_ans = []

for i in range(1,len(cards)) :
    if player_letter == cards[i][1] :
        possible_ans.append(cards[i][0])
        
#if more 
for i in range (len(possible_ans)) :
    if int(possible_ans[i]) > player_number and int(possible_ans[i]) < int(c):
        c = int(possible_ans[i]) #
        print(cards, f'{c}{player_letter}'  )
        found = True
    
print(possible_ans)
if found == False : 
    for i in range (len(possible_ans)) : 
               
        if int(possible_ans[i]) < int(d)  :
            d = int(possible_ans[i])

if found == False :       
    print(cards, f'{d}{player_letter}')
        

  











    