#           Part A — Intermediate Problems

#1
# while True:
#     marks = int(input("Enter marks between 0 and 100: "))

#     if 0 <= marks <= 100:
#         print("Valid marks")
#         break
#     else:
#         print("Invalid marks. Try again.")

#2

# while True:
#     num = int(input("Enter an integer greater than 0: "))

#     if num > 0:
#         break

# print("Accepted number:", num)

#3

# while True:
#     age = int(input("Enter your age here: "))
#     if 0 <= age <= 120:
#         print("Age accept")
#         break
#     else:
#         print("Not accept")

#4

# print('''1. View profile
# 2. Edit profile
# 3. Settings
# 4. Exit''')
# while True:
#     num = int(input("Enter your option here: "))
#     match num:
#         case 1:
#             print("View Profile")
#         case 2:
#             print("Edit profile")
#         case 3:
#             print("Setting")
#         case 4:
#             print("Exit")
#         case _:
#             print("Enter valid number 1-4!!!!")
#     if 1 <= num <= 4:
#         print("Valid output")
#         break
#     else:
#         print("Enter valid input!!!!")


#5

# password=input("Enter password: ")
# confirm=input("Confirm password: ")

# if len(password)>=8 and password==confirm:
#     print("Valid Password")
# else:
#     print("Invalid Password")

#6
# while True:
#     temp=int(input("Enter temperature here: "))
#     if -20<=temp<=40:
#         print("Valid")
#         break
#     else:
#         print("Invalid tempt")

#7

# balance = 0
# while True:
#     balance = int(input("Enter your balance here: "))
#     withdrawal = int(input("Enter withdrawal amount: "))

#     if 1 <= withdrawal <= balance:
#         print("Withdrawal Successfully!!")
#         break
#     else:
#         print("Enter Withdrawal is not enough")

#8


# username = input("Enter username: ").strip()

# while True:
#     if len(username) < 5 or " " in username:
#         print("Invalid username! Try again.")
#         username = input("Enter username: ").strip()
#     else:
#         break

# print("Accepted username:", username)


#9

# num = int(input("Enter a positive integer divisible by 3 and 5: "))

# while num <= 0 or num % 3 != 0 or num % 5 != 0:
#     print("Invalid number! Try again.")
#     num = int(input("Enter a positive integer divisible by 3 and 5: "))

# print("Accepted number:", num)

#10

# original = 2468
# attempt = 0

# while True:
#     pin = int(input("Enter your pin here: "))
#     if original == pin:
#         # attempt+=1
#         print("Welcome")
#         break
#     elif attempt<=3:
#         attempt+=1
#         print("Enter valid pin !!!!")

# original = 2468
# attempt = 0

# while attempt<=3:
#     pin=int(input("enter your pin :"))
#     if pin==original:
#         print("welcome")
#         break
#     elif attempt<=3:
#         attempt+=1    
#         print("try again")
#     else:
#         break    

#11

# number = int(input("Enter your number: "))

# while True:
#     if 10 <= number <= 50:
#         if number % 2 == 0:
#             print("Even")
#         else:
#             print("Odd")
#         break
#     else:
#         print("Number must be between 10 and 50.")
#         number = int(input("Enter your number: "))

#12

# balance = int(input("Enter your balance here: "))
# while True:
#     deposit = int(input("Enter your deposit amount here: "))
#     if deposit >= 0:
#         if deposit == balance:
#             print("Deposit Successfully")
#             break
#         else:
#             print("Enter valid deposit!!")
#     else:
#         print("Enter valid deposit!!")

#          Part B — Challenging Problems

#13

# number=0
# while True:
#     number=int(input("Enter number here: "))
#     if 1<=number<=100:
#         print(number)
#         break
#     else:
#         print("Enter valid number 1 to 100")

#14
# marks=0
# while True:
#     marks = int(input("Enter marks between 0 and 100: "))

#     if 0 <= marks <= 100:
#         if marks>=75:
#             print("Distinction!!")
#         elif 60<=marks<75:
#             print("First class")
#         elif 35<=marks<60:
#             print("Pass")
#         else:
#             print("Fail")
#     else:
#         print("Please enter valid number here:")

#15

# username=input("Enter your username here: ")
# password=input("Enter password: ")

# while len(username)<5 or " " in username or len(password.strip())==0 or len(password)<8:
#     print("Invalid username or password!! Try again.")

#     username=input("Enter username: ").strip()
#     password=input("Enter password: ")
# print("Username and password accepted successfully!!!")

#16

# num1=float(input("Enter first number: "))
# operator=input("Enter operator(+,-,*,/): ")

# while operator not in ["+","-","*","/"]:
#     print("Invalid opertor! Try again.")
# num2=float(input("Enter second number: "))
# while operator =="/" and num2==0:
#     print("Division by zero is not allowed!!")
#     num2=float(input("Enter your Second number: "))

# if operator=="+":
#     result=num1+num2
# elif operator=="-":
#     result=num1-num2
# elif operator=="*":
#     result=num1*num2
# else:
#     result=(num1/num2)

# print("Result:",result)

#17


balance = 10000

while True:
    print("\n1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    while choice < 1 or choice > 4:
        print("Invalid choice! Try again.")
        choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current balance: ₹", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        while amount <= 0:
            print("Amount must be greater than zero!")
            amount = float(input("Enter deposit amount: "))

        balance = balance + amount
        print("Deposit successful!")
        print("New balance: ₹", balance)

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        while amount <= 0 or amount > balance:
            print("Invalid amount! Check the balance and try again.")
            amount = float(input("Enter withdrawal amount: "))

        balance = balance - amount
        print("Withdrawal successful!")
        print("New balance: ₹", balance)

    elif choice == 4:
        print("Thank you for using our banking system!")
        break
#18

month = int(input("Enter month (1-12): "))

while month < 1 or month > 12:
    print("Invalid month!")
    month = int(input("Enter month (1-12): "))

day = int(input("Enter day (1-31): "))

while day < 1 or day > 31:
    print("Invalid day!")
    day = int(input("Enter day (1-31): "))

print("Accepted month:", month)
print("Accepted day:", day)

#19

quantity = int(input("Enter product quantity: "))

while quantity <= 0:
    print("Quantity must be a positive integer!")
    quantity = int(input("Enter product quantity: "))

price = float(input("Enter unit price: "))

while price <= 0:
    print("Price must be greater than zero!")
    price = float(input("Enter unit price: "))

total = quantity * price

print("Total cost: ₹", total)


#20
