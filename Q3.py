def GetPassword():
    upper = False
    lower = False
    number = False
    symbol = False
    while True:
        try:
            password = str(input('Password: '))
            if len(password) < 7 or 'password' in password.lower():
                raise Exception            
            for letter in password:
                if letter.islower():
                    lower = True
                elif letter.isupper():
                    upper = True
                elif letter.isdigit():
                    number = True
                else:
                    symbol = True
                if lower and upper and number and symbol:
                    return password
            if not (lower and upper and number and symbol):
                raise Exception
        except:
            print('Invalid Password. Try Again!!!')
print('The password is', GetPassword())