# has_id=input("Enter only Yes/No: ").strip().lower()
# if has_id=="no":
#     print("Bring your id")
# elif has_id=="yes":
#     print("Welcome")
# else:
#     print("Enter valid number")

# str = input("Enter a string: ")

# if str == str[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# number=input("Enter a number: ")
# if number==number[::-1]:
#     print("Number is palindrome")
# else:
#     print("Number is not palindrome")


# for row in range(3):
#     for column in range(4):
#         print("*",end="")
#     print()

# str=input("Enter your String here: ").strip().lower()
# flag=True
# count=0
# for char in str:
#     if char=="o":
#         flag=False
#         print("Found")
#         count+=1
#         break
# print(count)
# if flag:
#     print("Not found")

# for i in range(1,6):
#     if i==4:
#         break
#     print(i)

# for i in range(1,6):
#     if i==4:
#         break
#     print(i)

# for i in range(1,6):
#     if i==4:
#         continue
#     print(i)

# i=1
# while i<=5:
#     if i==3:
#         i+=1
#         continue
#     print(i)
#     i+=1

# for i in range(1,4):
#     for j in range(1,4):
#         if j==2:
#             break
#         print(i,j)

# for i in range(1,4):
#     if i==2:
#         break
# else:
#     print("Done")

# numbers=[10,-5,20,0,30]
# for n in numbers:
#     if n<0:
#         continue
#     if n==0:
#         break
#     print(n)
# for i in range(1,10):
#     if i==6:
#         break
#     print(i)

# number=[10,20,30,40]
# for value in number:
#     if value==30:
#         break
#     print(value)

# num = int(input("Enter your number here: "))
# for num in range(1, num):
#     if num == 0:
#         print("Number is zero")
#         break
# else:
#     print("Number is not zero")

# for i in range(1,101):
#     if i%7==0:
#         break
#     print(i)


# for i in range(1,20):
#     if i%2==0:
#         continue
#     print(i)

# numbers = [10, -2, 30, -5, 40, -8]
# for number in numbers:
#     if number < 0:
#         continue
#     print(number)

# for i in range(1,20):
#     if i%3==0:
#         continue
#     print(i)

# numbers = [5, 12, 8, 21, 30, 7]
# for number in numbers:
#     if number<=10:
#         continue
#     print(number)

# number=int(input("Enter your number here: "))
# if number>=0:
#     pass


# def first():
#     print("A")

# def second():
#     print("B")

# second()
# first()
# second()

# def calculate():
#     a = 10
#     b = 3

#     print("Addition:", a + b)
#     print("Subtraction:", a - b)
#     print("Multiplication:", a * b)
#     print("Division:", a / b)
#     print("Floor Division:", a // b)
#     print("Remainder:", a % b)
#     print("Power:", a ** b)

# calculate()

# a = 0
# b = 0

# def calculator():
#     for i in range(1, 10):
#         a = int(input("Enter number1 here: "))
#         b = int(input("Enter your number2 here: "))
#         print("1-Add,2-sub, 3-multiply, 4-division, 5-floor division, 6-Remainder, 7-power")

#         option = int(input("Enter your option you want to print: "))

#         if option == 1:
#             print(a + b)
#         elif option == 2:
#             print(a - b)
#         elif option == 3:
#             print(a * b)
#         elif option == 4:
#             print(a / b)
#         elif option == 5:
#             print(a // b)
#         elif option == 6:
#             print(a % b)
#         elif option == 7:
#             print(a ** b)
#         else:
#             print("Enter valid number 1-7!!!!!")


# calculator()

# a=0
# b=0


# def greet(name):
#     print("Hello",name)
# greet("Aman")

# def add(a,b):
#     return a+b
# result=add(10,20)
# print(result)

# def substract(a,b):
#     return a-b
# print(substract(10,7))
# print(substract(20,7))

# def greet(name="Guest"):
#     print("Hello",name)

# greet()
# greet("Aman")

# def student(name,age):
#     print(name,age)
# student(age=18,name="Aman")

# def calculator(a,b):
#     return a+b,a-b
# x,y=calculator(10,10)
# print(x,y)

# def calculator(a,b=5):
#     return a*b
# print(calculator(4))
# print(calculator(4,3))


# def addition(a,b):
#     c=a+b
#     print(c)
# a=int(input("Enter your number 1: "))
# b=int(input("Enter your number 2: "))
# addition(a,b)

# def add(a,b):
#     return a+b
# result=add(10,20)
# print(result)

# def square(num):
#     return (num*num)
# result=square(5)
# print(result)

# def greet(name="Guest"):
#     print("Hello",name)
# greet()
# greet("Aman")

# def add(a,b):
#     c=a+b
#     print(c)
# add(10,20, )
# def print_line():
#     print("--------------------")

# print("Student Report")
# print_line()
# print("Name: Asha")
# print_line()
# print("Marks: 85")
# print_line()

# def print_heading():
#     print("STUDENT REPORT")
#     print("----------------")

# def print_student_details():
#     print("Name: Asha")
#     print("Roll number: 12")

# def print_result():
#     print("Marks: 85")
#     print("Result: Pass")

# print_heading()
# print_student_details()
# print_result()

# def double(number):
#     return number*2
# def add_five(number):
#     return number+5
# result=add_five(double(10))
# print(result)


# a = 0
# b = 0

# def calculator():
#     while True:
#         a = int(input("Enter number1 here: "))
#         b = int(input("Enter your number2 here: "))
#         print("1-Add,2-sub, 3-multiply, 4-division, 5-floor division, 6-Remainder, 7-power")

#         option = int(input("Enter your option you want to print: "))

#         if option == 1:
#             print(a + b)
#         elif option == 2:
#             print(a - b)
#         elif option == 3:
#             print(a * b)
#         elif option == 4:
#             print(a / b)
#         elif option == 5:
#             print(a // b)
#         elif option == 6:
#             print(a % b)
#         elif option == 7:
#             print(a ** b)
#         else:
#             print("Enter valid number 1-7!!!!!")


# calculator()


# def print_line():
#     print("--------------------------")
# print("Student Report")
# print_line()
# print("Name: AMAN")
# print_line()
# print("Marks: 85")
# print_line()



# def greet(name):
#     print("Hello",name)
# greet("Aman")

# def show_number(number):
#     print(number)
# show_number(25)
# show_number(100)

# def add(a, b):
#     print(a + b)

# add(10, 20)


# def add(a,b):
#     return a+b
# result=add(10,20)
# print(result)

# def add(a, b):
#     print(a + b)

# answer = add(2, 3)
# print("Answer:", answer)

# def add(a, b):
#     return a + b
# answer = add(2, 3)
# print("Answer:", answer)

# def check():
#     print("Before return")
#     return 10
#     print("After return")
# value = check()
# print(value)

# def square(number):
#     result=number*number
#     return result
# print(square(5))

# def get_message():
#     message="Welcome to Python"
#     return message
# text=get_message()
# print(text)



# def mult(a,b):
#     return a*b
# product=mult(10,20)
# print(product)

# def square(number):
#     return number * number
# print(square(3)+ square(4))

# def is_even(number):
#     return number%2==0
# if is_even(8):
#     print("Even")
# else:
#     print("Odd")

# def calculator (a,b):
#     total= a+b
#     diff=a-b
#     product=a*b
#     return total,diff,product
# answer=calculator(10,5)
# print(answer)

# def greet(name="MD"):
#     print("Hello",name)
# greet()
# greet("Aman")

# def introduce(name,city="Pune"):
#     print(name,"is from",city)
# introduce("Aasha")


# def introduce(name,age):
#     print(name,age)
# introduce(age=19,name="Aman",)

# def order(item,quantity=1,price=100):
#     print(item,quantity,price)
# order("Notebook")
# order("Notebook",price=50)
# order("Notebook",3)
# order("Notebook",3,50)
# n = input("Enter a number: ")
# print(n * 2)

# x = 0

# if x:
#     print("Yes")
# else:
#     print("No")

# text = "  hello python  "
# print(text.strip().upper())

# def counter_fun(count):
#     count=count+1

#     if (count==5):
#         return count
    
#     counter_fun(count)
# print(counter_fun(1))