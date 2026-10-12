#1
num=int(input("Enter your number here: "))
if num%2==0:
    print("Number is even")
else:
    print("Number is odd")

#2
num1=int(input("Enter your number 1 here:"))
num2=int(input("Enter your number 2 here: "))

if num1>num2:
    print(num1)
else:
    print(num2)

#3
num1=int(input("Enter your number 1 here:"))
num2=int(input("Enter your number 2 here: "))
num3=int(input("Enter your num 3 here:"))
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)

#4

num=int(input("Enter your number here:"))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")

#5

age=int(input("Enter your age here:"))
if age<=12:
    print("Child")
elif age>=19:
    print("Teenager")
else:
    print("Adult")