def GetElementAt(list, index):
    try:
        print(list[index])
    except:
        print("None")
    finally:
        print("mission completed")    
GetElementAt([1,2,3,4,5,6,7],4)  
GetElementAt([1,2,3],3)
