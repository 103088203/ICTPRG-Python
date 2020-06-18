def GetIpAddress():
    while True:
        try:
            ipaddress = str(input('IP Address: '))
            ip_str = ipaddress.split('.')
            ip = [int(i) for i in ip_str]
            if ip[0] == 127 or len(ip) != 4:
                print('Invalid IP Address. Try Again!!!')
                continue
            if (ip[0] >= 1 and ip[0] <= 254) and (ip[3] >= 0 and ip[3] <= 254):
                if (ip[1] >= 0 and ip[1] <= 255) and (ip[2] >= 0 and ip[2] <= 255):
                    return ipaddress
            else:
                 print('Invalid IP Address. Try Again!!!')
        except:
            print('Invalid IP Address. Try Again!!!')
print('The IP Address is', GetIpAddress())