# i=1
# while i<=10:
#     print(i)
#     i+=1

# i=2
# while i<=20:
#     print(i)
#     i*=1

# count=2
# while count<=20:
#     print(count)
#     count+=2

# i=10
# while i>=1:
#     print(i)
#     i-=1

# i=3
# while i<=3:
#     print("*",end=" ")
#     i+=1

# number=int(input("Enter a number here:"))
# while number !=0:
#     print("You entered:",number)
#     number=int(input("Enter here number:"))
# print("Loop ended")

# number = int(input("Enter a number: "))

# while number != 0:
#     print("You entered:", number)
#     number = int(input("Enter a number: "))

# print("Loop ended")

# number = int(input("Enter a number: "))
# total = 0
# while number != 0:
#     total = total + number
#     number = int(input("Enter a number: "))
# print("Sum:", total)

# number=float(input("Enter a number here:"))
# while number !=0:
#     print("Your number:",number)
#     number=float(input("Enter a number here:"))
# print("Loop ended here!!!")

# number=float(input("Enter a number1:"))
# total=0
# while number !=0:
#     total=total+number
#     print(f"Debugging: number:{number},Total:{total}")
#     number=float(input("Enter a number here2:"))

# n=input("Enter a word:")
# char=0
# length=len(n)
# while char<=len(n)-1:
#     print(n[char[length,0,-1]])
#     char -= 1
#     if char ==n:
#         print("Number is palindrome")
#     else:
#         print("Number is not palindrome")


# str1=input("Enter string:")
# rstr=""
# i=len(str1)-1
# while i>=0:
#     rstr+=str1[i]
#     i-=1
# if str1==rstr:
#     print("String is palindrome.")

# i=1
# while i<=4:
#     print("* * * *")
#     i+=1

# i=1
# while i<=6:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1

#method2
# i=1
# while i<=5:
#     if i==1:
#         print("*")
#     elif i==2:
#         print("* *")
#     elif i==3:
#         print("* * *")
#     elif i==4:
#         print("* * * *")
#     else:
#         print("* * * * *")
#     i+=1

# i=1
# while i<=6:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j+=1
#     print()
#     i+=1

# str = input("Enter a sentence here:")
# flag = True
# i = 0
# j = len(str) - 1

# while i < j:
#     if str[i] != str[j]:
#         flag = False
#     i += 1
#     j -= 1

# if flag:
#     print("Sentence is palindrome!!")
# else:
#     print("Sentence is not palindrome!!!!!")

#method2
# str1=input("Enter a str1:")
# i=0
# j=len(str1)-1
# flag=True
# while i<j:
#     if str1[i]==str1[j]:
#         i+=1
#         j-=1
#     else:
#         flag=False
#         i=j
# if flag:
#     print("Palindrome")
# else:
#     print("Not palindrome!!!")

# number=472
# while number>0:
#     digit=number%10
#     print(digit)
#     number=number//10
# print(f"number=:",number, "Digit=:",digit)

# number=int(input("Enter a number here:"))
# total=0
# while number>0:
#     digit=number%10
#     total=total+digit
#     number=number//10
# print("Sum:",total)

# number=int(input("Enter a number here:"))
# i=number
# j=number-1
# flag=True
# while i<j:
#     if(number(i)==number(j)):
#         i+=1
#         j-=1
#     else:
#         flag=False
#         i=j
# if flag:
#     print("Number is palindrome!!!")
# else:
#     print("Number is not palindrome!!!!")

# number=int(input("Enter a number here:"))
# reverse=0
# while number>0:
#     digit=number%10
#     reverse= reverse*10 + digit
#     number=number//10
# print("Reverse:",reverse)
# str1=input("Enter sentence here to find plindrome or not:")
# i=0
# j=len(str1)-1
# flag=True
# while(i<j):
#     if(str1[i]==str1[j]):
#         i+=1
#         j-=1
#     else:
#         flag=False
#         i=j
# if flag:
#     print("String is palindrome!!!")
# else:
#     print("String is not palindrome")

# str = input("Enter a sentence here:")
# flag = True
# i = 0
# j = len(str) - 1

# while i < j:
#     if str[i] != str[j]:
#         flag = False
#     i += 1
#     j -= 1

# if flag:
#     print("Sentence is palindrome!!")
# else:
#     print("Sentence is not palindrome!!!!!")

# number=int(input("Enter a number here!!:"))
# total=0
# while number !=0:
#     total+=number
#     print("Total:",total)
#     number=int(input("Enter number:"))
# print("Loop ended!!")

# number=float(input("Enter a number1:"))
# total=0
# while number !=0:
#     total=total+number
#     print(f"Debugging: number:{number},Total:{total}")
#     number=float(input("Enter a number here2:"))
# print("Loop ended!!!")

# number=472
# while number>0:
#     digit=number%10
#     print(digit)
#     number=number//10

# number=float(input("Enter number here:"))
# total=0
# while number>0:
#     digit=number%10
#     total+=digit
#     number=number//10
# print("Sum:",total)

# number=float(input("Enter a number here:"))
# reverse=0
# while number>0:
#     digit=number%10
#     reverse=reverse*10 +digit
#     number=number//10
# print("Reverse:",reverse)

# i=1
# while i<=4:
#     print("* * * *")
#     i+=1

# i=1
# while i<=6:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1
#(---------------------------------------------)
# row=0
# while row<=3:
#     column=1
#     while column<=4:
#         print("*",end="")
#         column+=1
#     print()
#     row+=1/


# number1=int(input("Enter number1:"))
# number2=int(input("Enter number2:"))
# value=int(input("Enter your choice (1-5):"))

# match value:
#     case 1:
#         print("Addition:",number1+number2)
#     case 2:
#         print("Subtraction:",number1-number2)
#     case 3:
#         print("Multiplication:",number1*number2)
#     case 4:
#         print("Division:",number1/number2)
#     case 5:
#         print("Modulus:",number1%number2)
#     case _:
#         print("Invalid choice")

# color=input("Enter your traffic light color:")
# match color:
#     case "Red":
#         print("Stop")
#     case "Yellow":
#         print("Ready")
#     case "Green":
#         print("Go")
#     case _:
#         print("Invalid color")

# number1=int(input("Enter number1:"))
# number2=int(input("Enter number 2 here:"))
# print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus")
# value=1

# while value!=0:
#     value=int(input("Enter your choice (1-5):"))
    
#     match value:
#         case 1:
#             print("Addition:", number1 + number2)
#         case 2:
#             print("Subtraction:", number1 - number2)
#         case 3:
#             print("Multiplication:", number1 * number2)
#         case 4:
#             print("Division:", number1 / number2)
#         case 5:
#             print("Modulus:", number1 % number2)
#         case 0:
#             print("Exiting...")
#         case _:
#             print("Invalid choice")


# number1=0
# number2=0
# print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus")
# value=1

# while value != 0:
#     number1 = int(input("Enter number1:"))
#     number2 = int(input("Enter number2:"))
#     value = int(input("Enter your choice (1-5):"))
#     if value == 0:
#         print("Exiting...")
#         break
#     match value:
#         case 1:
#             print("Addition:", number1 + number2)
#         case 2:
#             print("Subtraction:", number1 - number2)
#         case 3:
#             print("Multiplication:", number1 * number2)
#         case 4:
#             print("Division:", number1 / number2)
#             if number2 == 0:
#                 print("Error: Division by zero is not allowed.")
#             else:
#                 print("Division:", number1 / number2)
#         case 5:
#             print("Modulus:", number1 % number2)
#         case _:
#             print("Invalid choice")


# day=int(input("Enter your day here:"))

# match day:
#     case 1|2|3|4|5:
#         print("Weekday")
#     case 6|7:
#         print("Weekend")
#     case _:
#         print("Invalid day")

# marks=int(input("Enter your marks here:"))

# match marks:
#     case x if x>=90:
#         print("A")
#     case x if x>=75:
#         print("B")
#     case x if x>=60:
#         print("C")
#     case x if x>=40:
#         print("D")
#     case _:
#         print("F")

number = int(input("Enter your choice (1-3):"))
customer = True

match customer:
    case True:
        match number:
            case 1:
                print("Hello, How are you?")
            case 2:
                print("Namaste, Aap kaise ho?")
            case 3:
                print("Bonjour, Comment ça va?")
            case _:
                print("Invalid choice")
    case False:
        match number:
            case 1:
                print("If you want to speak in English, please select 1.")
            case 2:
                print("If you want to speak in Hindi, please select 2.")
            case 3:
                print("If you want to speak in French, please select 3.")
            case _:
                print("Invalid choice. Please select a valid option.")
