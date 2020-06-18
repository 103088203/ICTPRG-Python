def GetEmailAddress():
    while True:
        try:
            mail=input("Enter a valid email address: ")
            if "@" in mail:
                name=mail.split("@")
                if (len(name[0])>2 and len(name[0]) <=32) and (len(name[1]) > 2 and len(name[1])<=32) and "." in name[1]:
                    return mail
                else:
                    raise Exception
            else:
                raise Exception
        except:
            print("This is not a valid email address. Try again!!!")
print("The valid email address is: ", GetEmailAddress())                
