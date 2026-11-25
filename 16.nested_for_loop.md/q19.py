N=int(input("Enter your number here: "))
for i in range(1,N+1):
    for j in range(1,N+1):
        if(i*j)%2==0:
            print(i,j,i*j)
    # print()