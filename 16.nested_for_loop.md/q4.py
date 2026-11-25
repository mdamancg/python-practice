row=int(input("Enter your row here: "))
column=int(input("Enter your column here: "))

for i in range(0,row):
    for j in range(0,column):
        print((i,j),end=" ")
    print()