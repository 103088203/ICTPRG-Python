def GetIpAddress():
    while True:
        try:
            ipadd=str(input("Enter the ipaddress: "))
            ipdot=ipadd.split(".")
            ip=[int(i) for i in ipdot]
            if ip[0] == 127 or len(ip) != 4:
                raise Exception  
            if (ip[0]>=1 and ip[0]<=254) and ip[3]<=254 and (ip[1]>=0 and ip[1]<=255) and (ip[2]>=0 and ip[2]<=255): 
                return ipadd
            else:
                print("Invalid ipaddress, try again!")
        except:
            print("Invalid ipaddress, try again!")
print("The ipaddress", GetIpAddress(), "is valid")            
