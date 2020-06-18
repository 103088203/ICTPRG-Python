def GetPassword():
    low= False
    up= False
    num= False
    sym= False
    while True:
        try:
            pwd=str(input("Enter the password: "))
            if len(pwd) < 7 or "password" in pwd.lower():
                raise Exception
            for x in pwd:
                if x.islower():
                    low= True
                elif x.isupper():
                    up = True
                elif x.isdigit():
                    num = True
                else:
                    sym = True
                    return pwd
            if not (low and up and num and sym):
                raise Exception  
        except:
            print("Invalid Password. Try again!!!")                
print("The password is", GetPassword())              

