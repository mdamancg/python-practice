n=int(input("Enter a number here: "))
for i in range(0,n+1):
    for j in range(0,n+1):
        if i==j:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()