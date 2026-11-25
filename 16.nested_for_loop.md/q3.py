row=int(input("Enter your row here:"))
column=int(input("Enter your column here: "))

for i in range(1,row+1):
    for j in range(1,column+1):
        print("*",end=" ")
    print()