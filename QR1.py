def GetElementAt(list, index):
    try:
        return list[index]
    except:
        return "None"
#    finally:
#        return "mission completed"        
print(GetElementAt([1,2,3,4,5,6,7],4))
print(GetElementAt([1,2,3],3))