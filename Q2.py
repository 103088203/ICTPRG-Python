def Input_Number():
    while True:
        try:
            n = int(input("Enter a valid number: "))  
            return n
        except ValueError:
            print("This is not a valid number, try again")
print(Input_Number(), "is a valid number")