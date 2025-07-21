#password

password = input('Please enter your password: ')
length = False 
class Check_Password(): 
    def __init__(self):
        pass 
    def length_check (self) :
        if len(password) < 8 : 
            print('Your password must be 8 characters or more long')
        else : 
            length = True
    def uppercase_check (self):
        for i in password : 
            if i.isupper() : 
                return True 
            else:
                print('Your password must have one uppercase letter')










