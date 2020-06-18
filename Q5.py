def GetEmailAddress():
    while True:
        try:
            email = str(input('Email address: '))
            if '@' in email:
                elements = email.split('@')
                if len(elements) == 2:
                    if len(elements[0]) > 2 and len(elements[0]) < 32 and len(elements[1]) > 2 and len(elements[1]) < 32 and '.' in elements[1]:
                        return email
                    else:
                        raise Exception
                else:
                    raise Exception
            else:
                raise Exception
        except:
            print('Invalid Email address. Try Again!!!')

print('The Email address is', GetEmailAddress())