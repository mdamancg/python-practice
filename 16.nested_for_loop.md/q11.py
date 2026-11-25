row=int(input("Enter your row here: "))
column=int(input("Enter your column here: "))
for i in range(row):
    # if i %2==0:
        for j in range(2,column+1,2):
            # if j % 2 == 0:
                print(j,end=" ")
        print()