for i in range(1,5):
    for j in range(1,5):
        if i%j==0:
            print("X",end=" ")
        else:
            print("-",end=" ")
    print()