n=int(input("Enter your number here: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print("Same",end=" ")
        else:
            print("Difference",end=" ")
    print()