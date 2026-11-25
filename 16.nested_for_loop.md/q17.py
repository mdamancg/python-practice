n=int(input("Enter your number here: "))
for i in range(1,n+1):
    for j in range(i,n+1):
        if j%(i+1)==0 or i==1 or j==i:
            print(j,end=" ")
    print()