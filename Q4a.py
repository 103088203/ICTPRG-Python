#fact_no=int(input("Enter the factorial number: "))
store=[]
for x in range(1,11):
    prod=1
    store.append(x)
    for i in store:
        prod = prod*i
    n_string = "x".join(str(y) for y in store)
    if x==1:
        print("%d = -> %d" % (x, prod))
    else:
        print("%d = %s -> %d" % (x, n_string, prod))    
