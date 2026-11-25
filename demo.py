# # has_id=input("Enter only Yes/No: ").strip().lower()
# # if has_id=="no":
# #     print("Bring your id")
# # elif has_id=="yes":
# #     print("Welcome")
# # else:
# #     print("Enter valid number")

# # str = input("Enter a string: ")

# # if str == str[::-1]:
# #     print("Palindrome")
# # else:
# #     print("Not Palindrome")


# # number=input("Enter a number: ")
# # if number==number[::-1]:
# #     print("Number is palindrome")
# # else:
# #     print("Number is not palindrome")


# # for row in range(3):
# #     for column in range(4):
# #         print("*",end="")
# #     print()

# # str=input("Enter your String here: ").strip().lower()
# # flag=True
# # count=0
# # for char in str:
# #     if char=="o":
# #         flag=False
# #         print("Found")
# #         count+=1
# #         break
# # print(count)
# # if flag:
# #     print("Not found")

# # for i in range(1,6):
# #     if i==4:
# #         break
# #     print(i)

# # for i in range(1,6):
# #     if i==4:
# #         break
# #     print(i)

# # for i in range(1,6):
# #     if i==4:
# #         continue
# #     print(i)

# # i=1
# # while i<=5:
# #     if i==3:
# #         i+=1
# #         continue
# #     print(i)
# #     i+=1

# # for i in range(1,4):
# #     for j in range(1,4):
# #         if j==2:
# #             break
# #         print(i,j)

# # for i in range(1,4):
# #     if i==2:
# #         break
# # else:
# #     print("Done")

# # numbers=[10,-5,20,0,30]
# # for n in numbers:
# #     if n<0:
# #         continue
# #     if n==0:
# #         break
# #     print(n)
# # for i in range(1,10):
# #     if i==6:
# #         break
# #     print(i)

# # number=[10,20,30,40]
# # for value in number:
# #     if value==30:
# #         break
# #     print(value)

# # num = int(input("Enter your number here: "))
# # for num in range(1, num):
# #     if num == 0:
# #         print("Number is zero")
# #         break
# # else:
# #     print("Number is not zero")

# # for i in range(1,101):
# #     if i%7==0:
# #         break
# #     print(i)


# # for i in range(1,20):
# #     if i%2==0:
# #         continue
# #     print(i)

# # numbers = [10, -2, 30, -5, 40, -8]
# # for number in numbers:
# #     if number < 0:
# #         continue
# #     print(number)

# # for i in range(1,20):
# #     if i%3==0:
# #         continue
# #     print(i)

# # numbers = [5, 12, 8, 21, 30, 7]
# # for number in numbers:
# #     if number<=10:
# #         continue
# #     print(number)

# # number=int(input("Enter your number here: "))
# # if number>=0:
# #     pass


# # def first():
# #     print("A")

# # def second():
# #     print("B")

# # second()
# # first()
# # second()

# # def calculate():
# #     a = 10
# #     b = 3

# #     print("Addition:", a + b)
# #     print("Subtraction:", a - b)
# #     print("Multiplication:", a * b)
# #     print("Division:", a / b)
# #     print("Floor Division:", a // b)
# #     print("Remainder:", a % b)
# #     print("Power:", a ** b)

# # calculate()

# # a = 0
# # b = 0

# # def calculator():
# #     for i in range(1, 10):
# #         a = int(input("Enter number1 here: "))
# #         b = int(input("Enter your number2 here: "))
# #         print("1-Add,2-sub, 3-multiply, 4-division, 5-floor division, 6-Remainder, 7-power")

# #         option = int(input("Enter your option you want to print: "))

# #         if option == 1:
# #             print(a + b)
# #         elif option == 2:
# #             print(a - b)
# #         elif option == 3:
# #             print(a * b)
# #         elif option == 4:
# #             print(a / b)
# #         elif option == 5:
# #             print(a // b)
# #         elif option == 6:
# #             print(a % b)
# #         elif option == 7:
# #             print(a ** b)
# #         else:
# #             print("Enter valid number 1-7!!!!!")


# # calculator()

# # a=0
# # b=0


# # def greet(name):
# #     print("Hello",name)
# # greet("Aman")

# # def add(a,b):
# #     return a+b
# # result=add(10,20)
# # print(result)

# # def substract(a,b):
# #     return a-b
# # print(substract(10,7))
# # print(substract(20,7))

# # def greet(name="Guest"):
# #     print("Hello",name)

# # greet()
# # greet("Aman")

# # def student(name,age):
# #     print(name,age)
# # student(age=18,name="Aman")

# # def calculator(a,b):
# #     return a+b,a-b
# # x,y=calculator(10,10)
# # print(x,y)

# # def calculator(a,b=5):
# #     return a*b
# # print(calculator(4))
# # print(calculator(4,3))


# # def addition(a,b):
# #     c=a+b
# #     print(c)
# # a=int(input("Enter your number 1: "))
# # b=int(input("Enter your number 2: "))
# # addition(a,b)

# # def add(a,b):
# #     return a+b
# # result=add(10,20)
# # print(result)

# # def square(num):
# #     return (num*num)
# # result=square(5)
# # print(result)

# # def greet(name="Guest"):
# #     print("Hello",name)
# # greet()
# # greet("Aman")

# # def add(a,b):
# #     c=a+b
# #     print(c)
# # add(10,20, )
# # def print_line():
# #     print("--------------------")

# # print("Student Report")
# # print_line()
# # print("Name: Asha")
# # print_line()
# # print("Marks: 85")
# # print_line()

# # def print_heading():
# #     print("STUDENT REPORT")
# #     print("----------------")

# # def print_student_details():
# #     print("Name: Asha")
# #     print("Roll number: 12")

# # def print_result():
# #     print("Marks: 85")
# #     print("Result: Pass")

# # print_heading()
# # print_student_details()
# # print_result()

# # def double(number):
# #     return number*2
# # def add_five(number):
# #     return number+5
# # result=add_five(double(10))
# # print(result)


# # a = 0
# # b = 0

# # def calculator():
# #     while True:
# #         a = int(input("Enter number1 here: "))
# #         b = int(input("Enter your number2 here: "))
# #         print("1-Add,2-sub, 3-multiply, 4-division, 5-floor division, 6-Remainder, 7-power")

# #         option = int(input("Enter your option you want to print: "))

# #         if option == 1:
# #             print(a + b)
# #         elif option == 2:
# #             print(a - b)
# #         elif option == 3:
# #             print(a * b)
# #         elif option == 4:
# #             print(a / b)
# #         elif option == 5:
# #             print(a // b)
# #         elif option == 6:
# #             print(a % b)
# #         elif option == 7:
# #             print(a ** b)
# #         else:
# #             print("Enter valid number 1-7!!!!!")


# # calculator()


# # def print_line():
# #     print("--------------------------")
# # print("Student Report")
# # print_line()
# # print("Name: AMAN")
# # print_line()
# # print("Marks: 85")
# # print_line()



# # def greet(name):
# #     print("Hello",name)
# # greet("Aman")

# # def show_number(number):
# #     print(number)
# # show_number(25)
# # show_number(100)

# # def add(a, b):
# #     print(a + b)

# # add(10, 20)


# # def add(a,b):
# #     return a+b
# # result=add(10,20)
# # print(result)

# # def add(a, b):
# #     print(a + b)

# # answer = add(2, 3)
# # print("Answer:", answer)

# # def add(a, b):
# #     return a + b
# # answer = add(2, 3)
# # print("Answer:", answer)

# # def check():
# #     print("Before return")
# #     return 10
# #     print("After return")
# # value = check()
# # print(value)

# # def square(number):
# #     result=number*number
# #     return result
# # print(square(5))

# # def get_message():
# #     message="Welcome to Python"
# #     return message
# # text=get_message()
# # print(text)



# # def mult(a,b):
# #     return a*b
# # product=mult(10,20)
# # print(product)

# # def square(number):
# #     return number * number
# # print(square(3)+ square(4))

# # def is_even(number):
# #     return number%2==0
# # if is_even(8):
# #     print("Even")
# # else:
# #     print("Odd")

# # def calculator (a,b):
# #     total= a+b
# #     diff=a-b
# #     product=a*b
# #     return total,diff,product
# # answer=calculator(10,5)
# # print(answer)

# # def greet(name="MD"):
# #     print("Hello",name)
# # greet()
# # greet("Aman")

# # def introduce(name,city="Pune"):
# #     print(name,"is from",city)
# # introduce("Aasha")


# # def introduce(name,age):
# #     print(name,age)
# # introduce(age=19,name="Aman",)

# # def order(item,quantity=1,price=100):
# #     print(item,quantity,price)
# # order("Notebook")
# # order("Notebook",price=50)
# # order("Notebook",3)
# # order("Notebook",3,50)
# # n = input("Enter a number: ")
# # print(n * 2)

# # x = 0

# # if x:
# #     print("Yes")
# # else:
# #     print("No")

# # text = "  hello python  "
# # print(text.strip().upper())


# # count1=0
# # def counter_fun(count):
# #     count=count+1

# #     if (count==20):
# #         # count1+=1
# #         return count
    
# #     return counter_fun(count)
# # print(counter_fun(1))

# # def greet():
# #     print("Hello world")
# # greet()

# # def show_welcome():
# #     print("Welcome to python!")
# #     print("Lets learn programming!!")
# # show_welcome()
# # show_welcome()
# # show_welcome()

# # def print_line():
# #     print("--------------------------------------")
# # print("Student Report")
# # print_line()
# # print("Name: Md Aman")
# # print_line()
# # print("Marks: 85")
# # print_line()

# # def greet(name):
# #     print("Hello",name)
# # greet("Aman")

# # def show_number(number):
# #     print(number)
# # show_number(25)
# # show_number(100)

# # def add(a,b):
# #     print(a+b)
# # add(5,6)

# # def introduce(name,city,age):
# #     print("Name:",name)
# #     print("Age:",age)
# #     print("City",city)
# # introduce("MD AMAN","SITAMARHI",19)

# # def subtract(a,b):
# #     print(a-b)
# # subtract(10,3)

# # def add(a,b):
# #     return a+b
# # result=add(10,20)
# # print(result)

# # def add(a,b):
# #     return a+b
# # result=add(2,5)
# # print("Answer:",result)

# # def square(number):
# #     result=number*number
# #     return result
# # print(square(5))

# # def get_message():
# #     message="Welcome to python"
# #     return message
# # text=get_message()
# # print(text)

# # def multiply(a,b):
# #     return a*b
# # result=multiply(2,5)
# # print(result)



# # def is_even(number):
# #     return number%2==0
# # if is_even(8):
# #     print("Even")
# # else:
# #     print("Odd")






# # def double(number):
# #     return number*2
# # def add_five(number):
# #     return number+5
# # result=add_five(double(10))
# # print(result)

# # def calculate(a,b):
# #     return a+b,a-b
# # total,diff=calculate(5,5)
# # print("Total:",total)
# # print("Difference:",diff)


# # def greet(name="Aman khan azad"):
# #     print("Hello",name)
# # greet()
# # greet("Md Naman Khan azad bin ramjan khalifa")

# # def introduce(name,city="Pune"):
# #     print(name,"Is from",city)
# # introduce("MD AMAN KHAN AZAD BIN RAMJAN KHALIFA")
# # introduce("Md Naman khan azad bin ramjan khalifa","mumbai")

# # def introduce(name,age):
# #     print(name,age)
# # introduce(name="Aman",age=19)


# # def info(a,b,c,*args):
# #     print(a,b,c)
# # info(2, 6, 7, 8, 9, 1, 2, 4, 5, 7)



# # def divide(a,b,/):
# #     return a/b
# # print(divide(10,2))

# # def greet(name,*,age):
# #     print(name,age)
# # greet("Aman",age=19)

# # def add_all(*args):
# #     return sum(args)
# # print(add_all(10,20,30))
# # print(add_all(10,20))
# # print(add_all())

# # def show_detail(**kwargs):
# #     print(kwargs)
# # show_detail(name="Aman",age=20)

# # def demo(name,*args,active=True,**kwargs):
# #     print(name)
# #     print(args)
# #     print(active)
# #     print(kwargs)
# # demo("Aman",10,20,active=False,city="Pune")

# # def add(a,b,c):
# #     return a+b+c
# # number=[10,20,30,40]
# # print(add(*number))

# # def introduce(name, age):
# #     print(name, age)

# # person = {"name": "Ravi", "age": 21}
# # introduce(**person)

# # a={"color": "Red"}
# # b={"color":"Blue","size":10}
# # result={**a,**b}
# # print(result)

# # def divide(c,d,/,*,a,b=2):
# #     return a/b,c+d
# # print(divide(4,5,a=10))

# # def add(*args):
# #     print(args)
# #     print(type(args))

# # add(10, 20, 30)

# # def add_all(*args):
# #     total=0
# #     for number in args:
# #         total +=number
# #     return total
# # print(add_all(10,20))
# # print(add_all(1,2,3,4))
# # print(add_all())


# # def divide(a,b,/,*,c,d):
# #     return a+b, c/d
# # print(divide(4,5,c=10,d=2))

# # def add(*args):
# #     print(args)
# #     print(type(args))
# # add(10,20,30)



# # def calculate(a,b,/,operation="add"):
# #     if operation=="add":
# #         return a+b
# #     if operation=="multiply":
# #         return a*b
# #     return None
# # print(calculate(3,4))
# # print(calculate(3,4,operation="multiply"))

# # def user_info(name,*,age,city):
# #     return f" My {name} i am {age} old and i am from {city}"
# # print(user_info("Aman",age=19,city="Pune"))


# # def book_ticket(source,destination,/,*,passenger,seat="Regular"):
# #     print(source,"to",destination)
# #     print("Passenger: ",passenger)
# #     print("Seat:",seat)
# # book_ticket("Pune","Mumbai",passenger="Md Aman",seat="Window")
# # book_ticket("Pune","Mumbai",passenger="Md Aman")


# # def example(pos_only,/,normal,*args,option=True,**kwargs):
# #     print(pos_only)
# #     print(normal)
# #     print(args)
# #     print(option)
# #     print(kwargs)
# # example(1,2,3,4,option=False,color="blue")

# # def add(*args):
# #     print(args)
# #     print(type(args))
# # add(10,20,30)


# # def add_all(*args):
# #     total=0
# #     for number in args:
# #         total +=number
# #     return total
# # print(add_all(10,20))
# # print(add_all(1,2,3,4))
# # print(type(add_all()))


# # def introduce(name,*hobbies):
# #     print("Name:",name)
# #     print("Hobbies:",hobbies)
# # introduce("Aman","Reading","cricket","music")

# # def show(*args):
# #     print(args[0])
# # show("Red","green")

# # def show(name,*args):
# #     print(name,args)
# # show("Aasha",["reading", "music"])

# # def show_detail(**kwargs):
# #     print(kwargs)
# #     print(type(kwargs))
# # show_detail(name="Aman khan",age=20, city="Pune")

# # def show_detail(**aman):
# #     print(aman)
# #     print(type(aman))
# # show_detail(name="Aman khan",age=20,city="Pune")

# # def show_details(**kwargs):
# #     for key, value in kwargs.items():
# #         print(key, "=", value)

# # show_details(name="Asha", age=20)

# # def show_details(**kwargs):
# #     for key,value in kwargs.items():
# #         print(key,"=",value)
# # show_details(name="Aman",age=20)

# # def greet(**kwargs):
# #     name=kwargs.get("name","Guest")
# #     print("Hello",name)
# # greet(name="Aasha")
# # greet()

# # def greet(**kwargs):
# #     name=kwargs.get("name","Guest")
# #     print("Hello",name)
# # greet(name="Aman khan azad")
# # greet()

# # def create_profile(name,**details):
# #     print("Name:",name)
# #     print("Other detail:",details)
# # create_profile("Aman",age=20,city="Pune")

# # def function():
# #     sen = input("Enter your sentence here: ").upper()
# #     target = input("Enter your target you want to find: ").upper()
# #     found = False
# #     for i in range(len(sen)):
# #         for j in range(len(target)):
# #             if sen[i] == target[j]:
# #                 print("Char is found:", sen[i])
# #                 found = True
# #                 break
# #     if not found:
# #         print("Char is not found")
# # function()



# # n=input("Enter your char here: ").upper()
# # for i in range(len(n)):
# #     count=0
# #     for j in range(len(n)):
# #         if n[i]==n[j]:
# #             count+=1
# #     if n.find(n[i])==i:
# #         print(n[i],"=",count)

# # def factorial():
# #     n=int(input("Enter your number here: "))
# #     for i in range(1,n+1):
# #         print(n*n)
# # factorial()

# # def calculate(length,width):
# #     """
# #     calcultate the are of reactangle.
# #     Args:
# #          length:The rectangle length.
# #          width:The rectangle width.
# #     Return:
# #           The area of the reactangle.
# #     """
# #     return length*width
# # print(calculate(5,4))
# # print(calculate.__doc__)


# # total=100
# # def calculate():
# #     total=100
# #     total +=10
# #     print(total)
# #     # total +=10
# # calculate()
# # print(total)
# # # print(total)
# # calculate()

# # x = 10
# # def demo():
# #     print(x)
# #     x = 20
# # demo()

# # x=10
# # def demo():
# #     global x
# #     x +=20
# #     print(x)
# # demo()

# # x=[]
# # def demo():
# #     global x
# #     print(x)
# # demo()

# # x=[]
# # def demo():
# #     x.append("Aman")
# #     print(x)
# # demo()
# # print(x)


# # number=int(input("Enter your number here: "))
# # for i in range(1,11):
# #     print(number*i)

# # name="Python"
# # for char in name:
# #     print(char)

# # number=int(input("Enter your number here: "))
# # reverse=0
# # while number>0:
# #     digit=number%10
# #     reverse=reverse*10+digit
# #     number=number//10
# # print("Reverse:",reverse)

# def calculate(a,b):
#     total=a+b
#     diff=a-b
#     return total,diff
# answer=calculate(10,4)
# print(answer)

# def calculate(a,b):
#     return a+b,a-b
# total,diff=calculate(10,4)
# print("Total:",total)
# print("Difference:",diff)

# def calculator(a,b):
#     return a+b,a-b
# total,diff=calculator(5,4)
# print("Total:",total)
# print("Different:",diff)


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


# x=10
# def demo():
#     print(x)
#     x=20
# demo()

# x=10
# def demo():
#     global x
#     print(x)
#     x=20
# demo()
# print(x)


# items=[]
# def add_items():
#     for i in range(1,5):
#         items.append(input("Enter your items here: "))    
# add_items()
# print(items)

# # list="Hello"
# def outer():
#     def inner():
#         # global list
#         print(list("Hello"))
#     inner()
# outer()

# def outer():
#     count=0
#     def increment():
#         nonlocal count
#         count+=1
#         return count
#     return increment
# counter=outer()
# print(counter())
# print(counter())
# print(counter())

# count=0
# def increment():
#     global count
#     count+=1
#     return count
# counter=increment()
# print(counter)
# print(counter)

# if True:
#     result=25
# print(result)

# def function():
#     if True:
#         result=25
#         print(result)
# function()

# def outer()
#                                      recursive case
# add=0
# def counter_fun(n):
#     global add
#     add+=n
#     if(n==10):
#         return add
#     return counter_fun(n+1)
# print(counter_fun(1))

# count=0
# def counter_fun(n):
#     global count
#     count+=1
#     if(count==5):
#         return count
#     counter_fun(n+1)
# print(counter_fun(1))

# count=0
# def counter_fun(n):
#     global count
#     count+=1
#     if(count==5):
#         return count
#     return counter_fun(n+1)
# print(counter_fun(1))

# add=0
# def counter_fun(n):
#     global add
#     add+=n
#     if(n==10):
#         return add
#     return counter_fun(n+1)
# print(counter_fun(1))

# def countdown(n):
#     if n==0:
#         print("Done")
#         return
#     print(n)
#     countdown(n-1)
# countdown(3)

# def show(n):
#     if n==0:
#         print("End")
#         return
#     print("Start:",n)
#     show(n-1)
#     print("Back:",n)
# show(2)

# def count_up_to(n):
#     if n==0:
#         print(0)
#         return
#     count_up_to(n-1)
#     print(n)
# count_up_to(3)

# def count_up_to(n):
#     if n==0:
#         print(0)
#         return
#     print(n)
#     count_up_to(n-1)
# count_up_to(3)

# def sum_to(n):
#     if n==0:
#         return 0
#     return n+sum_to(n-1)
# print(sum_to(4))

# def factorial(n):
#     if n==0:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))
# print(factorial(1))

