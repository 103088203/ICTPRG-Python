def InputNumber():
    while True:
        try:
            num=int(input("Enter a digit: "))
            return num
        except:
            print("This is not a valid digit. Try again")
print(InputNumber(), "is a valid digit")

