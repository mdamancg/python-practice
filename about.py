# # Name=input("Enter your name:")
# # Age=int(input("Enter your age:"))
# # Lab= input("Enter your lab:")
# # product_name= input("Enter your product name:")
# # product_price= float(input("Enter your product price:"))
# # quantity=int(input("Enter the quantity:"))
# # total_price= product_price * quantity
# # print("Your name is:", Name)
# # print("Your age is:", Age)
# # print("Your lab is:", Lab)
# # print("Product name:", product_name)
# # print("Product price:", product_price)
# # print("Quantity:", quantity)
# # print("Total price:", str(total_price))
# # d=input(product_name + " is " + str(total_price) + " in total price. Do you want to buy it? (yes/no):")
# # print("Your decision is:", d)
# num=int(input("Enter three digit number:"))
# a=num%10
# num=num//10
# b=num%10
# num=num//10
# print(a+b+num)

# sum=0
# for i in range (1,100):
#     sum=sum+i
#     average=sum/99
#     print(average)

# number=int(input("Enter your number:"))
# for i in range(number):
#     if i%2==0:
#         print(f"{i}number is even")

# str=input("Enter a string:").strip().lower()
# str2=""
# length=len(str)
# for element in range (length-1,-1,-1):
#     str2=str2+str[element]
# if str==str2:
#     print("String is palindrome")
# else:
#     print("String is not palindrome")

# number=input("Enter number:").strip()
# number2=""
# length=len(number)
# for i in range (length-1,-1,-1):
#     number2=number2+number[i]

# if number==number2:
#         print("Number is palindrome")
# else:
#         print("Number is not palindrome")

# name = "Python"

# for character in name:
#     print(character)

# word="python"
# count=0

# for character in word:
#      count=count+1
# print("characters:",count)

# for i in range(5):
#     for j in range(5):
#         print("*", end="")
#     print()
# for i in range(1,5):
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# num=int(input("Enter a number:"))
# for i in range(1,num):
#     for j in range(1,i+1):
#         print(j,end="")
#     print(j)

# num=int(input("Enter a number:"))
# for i in range(1,num):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# for i in range(1,11): #because last number is ending index so 11-1=10 tak print krega ye
#     print(i)

# for i in range(2,20,2):
#     print(i)
#     #2nd method
# for i in range(1,20):
#     if i%2==0:
#         print("Even number.")
#     else:
#         print("Odd number.")

# n=int(input("Enter a number:"))
# for i in range(1,n+1):
#     print(i)

# n=int(input("Enter a number:"))
# sum=0
# for i in range(1,n+1):
#   sum=sum+i
# print(sum)

# n = int(input("Enter a number:"))
# for i in range(1, 11):
#     print(n * i)

# n=int(input("Enter a number:"))
# factorial=1
# for i in range(1,n+1):
#     factorial=factorial*i
# print(factorial)

# name=input("Enter your name:")
# for character in name:
#     print(character)

# n=int(input("Enter a number:"))
# count=0
# for i in range(1,n+1):
#   if i%2==0:
#     count=count+1
# print("Total even number is:",count)


# largest=0
# for i in range(5):
#     n=int(input("Enter a number:"))

#     if n>largest:
#         largest=n
# print("Largest number is:",largest)
# smallest=0
# for i in range(5):
#     n=int(input("Enter a number:"))

#     if n<smallest:
#         smallest=n
# print("Smallest number is :",smallest)

# largest=int(input("Enter a number:"))
# for i in range(4):
#   n=int(input("Enter a number:"))
#   if n>largest:
#     largest=n
# print("Largest number:",largest)

# largest=int(input("Enter a number:"))
# for i in range(4):
#   n=int(input("Enter a number:"))
#   if n>largest:
#     largest=n
# print("Largest number:",largest)

# smallest=int(input("Enter a number:"))
# for i in range(4):
#    n=int(input("Enter a number:"))
#    if n<smallest:
#       smallest=n
# print("Smallest number:",smallest)

# print("Diffrence:",largest-smallest)
# #method2
# largest = int(input("Enter a number: "))
# smallest = largest

# for i in range(4):
#     n = int(input("Enter a number: "))

#     if n > largest:
#         largest = n

#     if n < smallest:
#         smallest = n

# print("Largest number:", largest)
# print("Smallest number:", smallest)
# print("Difference:", largest - smallest)

# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()

# n=int(input("Enter a number:"))
# for i in range(1,n+1):
#     for j in range(n-1):
#         print("*",end="")
#     print()
# num=int(input("Enter a number:"))
# for i in range(num,0,-1):
#      for j in range(1,num-i):
#          print(" ",end="")
#      for k in range(1,i+1):
#           print("*",end="")
#      print()

# for i in range(1,6):
#     for j in range(1,6-i):
#         print("",end=" ")
#         for k in range(2*i-1):
#             print("*",end="")
# print()

# total=0
# flag=True
# Grade=""
# for i in range(5):
#     marks=int(input("Enter your marks:"))
#     total +=marks
#     if marks<35:
#         flag=False
#     percentage=total/5

# if flag:
#     if percentage>=90:
#          Grade="A+"
#     elif percentage>=80:
#          Grade="A+"
#     elif percentage>=70:
#        Grade="B"
#     elif percentage>=60:
#         Grade="C"
#     elif percentage>=50:
#         Grade="D"
#     else:
#         Grade="F"
# if flag:
#     print(total,percentage,Grade)
# else:
#     print(f"your total marks is {total} and you are fail")

# total=0
# for i in range(5):
#     salary=int(input("Enter your salary:"))
#     total +=salary
#     Avg=total/5
# if Avg>=50000:
#     print("Highest salary")
# elif Avg>=30000:
#     print("Medium Salary")
# else:
#     print("Lowest salary")

# total=0
# for i in range(5):
#     unit=int(input("Enter your electricity Unit:"))
#     total +=unit

# if total>=100:
#     print(f"Your total bill is:{total*5}")
# elif unit<=200:
#     print(f"Your total bill is {(100*5)+((unit-100)*7)}")
# else:
#     print(f"Your total electricity bill is {(100*5)+(100*7)+((unit-200)*7)}")


# total = 0

# for i in range(5):
#     unit = int(input("Enter your electricity units: "))

#     if unit <= 100:
#         bill = unit * 5

#     elif unit <= 200:
#         bill = (100 * 5) + ((unit - 100) * 7)

#     else:
#         bill = (100 * 5) + (100 * 7) + ((unit - 200) * 10)

#     total += bill

# average = total / 5

# print("Total collection:", total)
# print("Average bill:", average)

# a=int(input("En"))

# for i in range(5):
#     password=input("Enter your password:")
#     score=0
#     uppercase=False
#     lowercase=False
#     digit=False
#     special=False

# if len(password)>=8:
#     score +=1
# for char in password:
#     if char >="A" and char<="Z":
#         uppercase=True
#     elif char>="a" and char <="z":
#         lowercase=True
#     elif char>="0" and char <="9":
#         digit=True
#     else:
#         special=True

# if uppercase:
#     score +=1
# if lowercase:
#     score+=1
# if digit:
#     score +=1
# if special:
#     score+=1
# if score==5:
#     print("Strong")
# elif score>=3:
#     print("Medium")
# else:
#     print("Weak")

# for i in range(5):
#     password = input("Enter password: ")

#     score = 0
#     uppercase = False
#     lowercase = False
#     digit = False
#     special = False

#     if len(password) >= 8:
#         score += 1

#     for char in password:

#         if char >= 'A' and char <= 'Z':
#             uppercase = True

#         elif char >= 'a' and char <= 'z':
#             lowercase = True

#         elif char >= '0' and char <= '9':
#             digit = True

#         else:
#             special = True


#     if uppercase:
#         score += 1

#     if lowercase:
#         score += 1

#     if digit:
#         score += 1

#     if special:
#         score += 1

    
#     if score == 5:
#         print("Strong")

#     elif score >= 3:
#         print("Medium")

#     else:
#         print("Weak")

# for i in range(5):
#     sentence=input("Enter your sentence here:")
#     lenght=len(sentence)
#     if lenght<=3:
#         print("Number is short")
#     elif lenght<=6:
#         print("Number is Medium")
#     else:
#         print("Number is Long")
# n=int(input("Enter a number:"))
# N=str(n)
# print(N,type(N))

# Take 5 numbers from the user.

# For each number:

# Convert it to a string.
# Examine every digit using a loop.
# Count even and odd digits.
# Print which type occurs more.
# If equal, print "Equal".
# Even=0
# Odd=
# for i in range(5):
#     n=input("Enter a Number or sentence here:")
#     Even=0
#     Odd=0
#     N=str(n)
#     length=len(n)

#     if int(length)%2==0:
#         Number1="Even"
#         Even +=1
#     else:
#         Number2="Odd"
#         Odd+=1

#     if even>odd:
#         print("even occurs more")
#     elif odd>even:
#         print("odd occurs more")

# text=input("Enter Sentence Here:")
# process=""

# for char in text:
#     if char in process:
#         continue
#         count=0
#     for c in text:
#         if c==char:
#             count+=1
#     if char>1:
#         process=char
#         if count==2:
#             category="Dublicate"
#         elif count<=4:
#             category="Repeated"
#         else:
#             category="Highly repeated"
#     print(f"{char} apper {count} times {category}")

# text = input("Enter a string: ")
# processed = ""

# for char in text:
#     if char in processed:
#         continue
#     count = 0
#     for i in text:
#         if i == char:
#             count += 1
#     if count > 1:
#         processed += char

#         if count == 2:
#             category = "Duplicate"
#         elif count <= 4:
#             category = "Repeated"
#         else:
#             category = "Highly Repeated"

#         print(f"'{char}' appears {count} times -> {category}")

# text=input("Enter your Sentence here:")
# vowel=0
# consonant=0
# digit=0
# special_character=0

# for char in text:
#     print(char)
#     for position in range(len(text)):
#         char = text[position]
#     if position%2==0:
#         number="Even"
#     else:
#         number="Odd"
#         if char.lower() in "aeiou":
#             chart_type="Vowel"
#             vowel+=1
#         elif char.isalpha():
#             chart_type = "Consonant"
#             consonant += 1
#         elif char.isdigit():
#             chart_type = "Digit"
#             digit += 1
#         else:
#             chart_type = "Special character"
#             special_character += 1
#         print(f"char:{char}|position:{position}| type:{chart_type}")

# print(f"Vowel:{vowel}")
# print(f"Consonant:{consonant}")
# print(f"Digits:{digit}")
# print(f"Special charater:{special_character}")

# for number in range(3):
# n = int(input("Enter a number here: "))
# for i in range(1, n + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("z")
#     elif i % 3 == 0:
#         print("x")
#     elif i % 5 == 0:
#         print("y")
#     else:
#         print("Invalid data")
#     print()

# n=int(input("Enter a number:"))
# for i  in range(1,n):
#     for j in range(n-1):
#         if j>=n:
#             print("*",end="")
#         else:
#             print("*",end="")
#     print()

# for i in range(5):
#     for j in range(5):
#         if i == 5 - 1 or j==0 or j == 5 - 1:
#             print("*", end="")
#         else:
#             print(" ",end="")
#     print()

# for i in range(1,6):
#     text=input(f"Enter username1 {i}:")
#     length=len(text)

#     digit_count=0
#     under_score=0
#     has_invalid_char=False

#     for char in text:
#         if char.isdigit():
#             digit +=1
#         elif char=="_":
#             under_score +=1
#         else:
#             has_invalid_char=True
#     if length == 0 or not text[0].isalpha() or text[0] == "_":
#         Status="Invalid"
#     elif digit==0 or under_score==0:
#         Status="Need Improvement"
#     else:
#         Status="Invalid"
#     print(f"\n--- Analysis for '{username}' ---")
#     print(f"Length: {length}")
#     print(f"First Character Valid: {first_char_valid}")
#     print(f"Digits: {digit_count}")
#     print(f"Underscores: {underscore_count}")
#     print(f"Invalid Special Characters Detected: {has_invalid_char}")
#     print(f"Classification: {status}\n")

# n=int(input("Enter a number here:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or j==n or i==n:
#             print("*",end="")
#         elif j==3 or n//2 or i==2:
#             print(" ",end="")

#         else:
#             print(" ",end="")
#     print()
# for i in range(1,6):
#     units=int(input(f"Enter your electricity Unit here{i}:"))
#     if units==100:
#         bill=units*5
#     elif units>100:
#         bill=units*7
#     elif units<=200:
#         bill=(100*5)+((units-100)*7)
#     else:
#         bill=(100*5)+(100*7)+((units-100)*15)
#     if bill<1000:
#         Status=("Low bill")
#     elif bill>=3000:
#         Status=("Medium bill")
#     else:
#         Status=("High bill")

#     print(f"Your bill is {bill} and your status is {Status}")

# vowel=0
# consonant=0

# for position in range(1,6):
#      sentence=input(f"Enter sentence here{position}:")

#      char=sentence[position]

#      if char.lower() in "aeiou":
#          Position_type="Vowel"
#          vowel +=1
#      else:
#          Position_type="Consonant"
#          consonant +=1

#      if vowel>consonant:
#          Status="Vowel Heavy"
#      elif consonant>vowel:
#          Status="Consonant Heavy"
#      elif vowel==consonant:
#          Status="Both are balanced"
#      else:
#          Status="Invalid!!!!"

# print(f"Your char type is {Position_type} and who heavy: {Status}")


# text=input("Enter your text here:")
# vowel=0
# consonant=0

# for position in range(len(text)):
#     char=text[position]
#     if position%2==0:
#         position_type="Even"
#     else:
#         position_type="Odd"

#     if char.lower() in "aeiou":
#         char_type="Vowel"
#         vowel+=1
#     elif char.isalpha:
#         char_type="Consonant"
#         consonant+=1
#     else:
#         char_type="Invalid data please enter character!!!"

#         if vowel>consonant:
#             Status="Vowel Heavy"
#         elif vowel<consonant:
#             Status="Consonant Won"
#         elif vowel==consonant:
#             Status="Both are equal"
#         else:
#             Status="Error"

#         print(f"Character:{char}|Position:{position}|{position_type}|type:{char_type}|Who is most heavy {Status}")

for i in range(6,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()