#1
for i in range(3):
    for j in range(3):
        print("*",end="")

#2

for i in range(3):
    for j in range(3):
        print(j,end="")
    print()
#3
for i in range(1,4):
    for j in range(i):
        print(i+1,end="")
    print()

#4
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

#5
for i in range(6,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

#6

for i in range(1,6):
    for j in range(i):
        print(j,end=" ")
    print()
#7
for i in range(1,6):
    for j in range(i):
        print(j+1,end=" ")
    print()

#8
for row in range(1,6):
    for column in range(1,row+1):
        print(i,end=" ")
    print()

#9

n=int(input("Enter a number here:"))
for i in range(1,n+1):
    for j in range(1,11):
        print(i*j,end=" ")
    print()

#10
n=int(input("Enter a number here:"))
for i in range(1,n+1):
    for j in range(1,6):
        print(i*j,end=" ")
    print()

#11
for i in range(1,6):
    for j in range(1,6):
        print(j**2,end=" ")
    print()

#12

n="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(1,27):
    for j in range(i):
        print(n[j], end=" ")
    print()

#13
n="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(1,27):
    for j in range(i):
        print(n[i], end=" ")
    print()

#14
for i in range(1,6):
    for j in range(1,i+1):
        print(j**2-1,end=" ")
    print()

#15
n=int(input("Enter a number here:"))
for i in range(n+1):
    for j in range(2*i+2):
        if j%2!=0:
            print(j,end=" ")
    print()

#16
n=int(input("Enter a number here:"))
for i in range(1,n+1):
    for j in range(1,2*i+2):
        if j%2==0:
            print(j,end="")
    print()

#17
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()

#18
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()

#19
number=0
for i in range(3):
    for j in range(3):
        number+=1
        print(number,end=" ")
    print()

#20
number=0
for i in range(5):
    for j in range(1,7):
        number+=1
        print(number,end=" ")
    print()

#21
number=0
for i in range(1,4):
    for j in range(1,4):
        number +=1
        print((i,j),end=" ")
    print()

#22
for i in range(1,4):
    for j in range(1,4):
        print(i,j)

#23
for i in range(10):
    for j in range(10):
        print("*",end="")
    print()

#24
for i in range(6):
    for j in range(i):
        print(i, end="")
    print()

#25
for i in range(6,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


#26
for i in range(5):
    for j in range(5):
        print(i+1 , end="")
    print()