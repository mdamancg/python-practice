# fail=0
# passed=0
# good=0
# excellent=0

# for i in range(10):
#     marks=int(input("Enter student marks:"))

# if marks<35:
#         print("Fail")
#         fail +=1
# elif marks<=49:
#         print("Passed")
#         passed +=1
# elif marks <=74:
#         print("Good")
#         good+=1
# elif marks <= 100:
#         print("Excellent")
#         excellent += 1
# print("Fail Students:",fail)
# print("Passed Student:",passed)
# print("Good Student:",good)
# print("Excellent Student:",excellent)

fail = 0
passed = 0
good = 0
excellent = 0

for i in range(10):
    marks = int(input("Enter marks: "))

    if marks < 35:
        print("Fail")
        fail += 1

    elif marks <= 49:
        print("Pass")
        passed += 1

    elif marks <= 74:
        print("Good")
        good += 1

    elif marks <= 100:
        print("Excellent")
        excellent += 1

print("Fail students:", fail)
print("Pass students:", passed)
print("Good students:", good)
print("Excellent students:", excellent)


for i in range(5):
    password = input("Enter password: ")

    score = 0
    uppercase = False
    lowercase = False
    digit = False
    special = False

    if len(password) >= 8:
        score += 1

    for char in password:

        if char >= 'A' and char <= 'Z':
            uppercase = True

        elif char >= 'a' and char <= 'z':
            lowercase = True

        elif char >= '0' and char <= '9':
            digit = True

        else:
            special = True


    if uppercase:
        score += 1

    if lowercase:
        score += 1

    if digit:
        score += 1

    if special:
        score += 1

    
    if score == 5:
        print("Strong")

    elif score >= 3:
        print("Medium")

    else:
        print("Weak")


for i in range(5):
    password = input("Enter password: ")

    score = 0
    uppercase = False
    lowercase = False
    digit = False
    special = False

    if len(password) >= 8:
        score += 1

    for char in password:

        if char >= 'A' and char <= 'Z':
            uppercase = True

        elif char >= 'a' and char <= 'z':
            lowercase = True

        elif char >= '0' and char <= '9':
            digit = True

        else:
            special = True


    if uppercase:
        score += 1

    if lowercase:
        score += 1

    if digit:
        score += 1

    if special:
        score += 1

    
    if score == 5:
        print("Strong")

    elif score >= 3:
        print("Medium")

    else:
        print("Weak")

for i in range(5):
    sentence=input("Enter your sentence here:")
    lenght=len(sentence)
    if lenght<=3:
        print("Number is short")
    elif lenght<=6:
        print("Number is Medium")
    else:
        print("Number is Long")


even=0
odd=0

for i in range(6):
    number=int(input("Enter your number here:"))
    Str=str(number)
    if number%2==0:
        Number="Even"
        even +=1
    else:
        Number="Odd"
        odd +=1
if even>odd:
    print("Even Occur more.")
elif even==odd:
    print("Odd and even are equal.")
else:
    print("Odd occur more.")

text = input("Enter a string: ")
processed = ""

for char in text:
    if char in processed:
        continue
    count = 0
    for i in text:
        if i == char:
            count += 1
    if count > 1:
        processed += char

        if count == 2:
            category = "Duplicate"
        elif count <= 4:
            category = "Repeated"
        else:
            category = "Highly Repeated"

        print(f"'{char}' appears {count} times -> {category}")


number=0
for i in range(8):
    price=float(input("Enter product price here:"))

    if price<500:
        budget="Budget"
        Avg=price/8
        number +=1
    elif price>=1999:
        budget="Regular"
        Avg=price/8
        number +=1
    elif price>=4999:
        budget="Premium"
        Avg=price/8
        number+=1
    else:
        budget="Luxury"
        Avg=price/8
        number+=1

print(f"Your budget is {budget} and your average product detail is {Avg} and number of product is {number}")


text = input("Enter your Sentence here: ")

vowel = 0
consonant = 0
digit = 0
special_character = 0

for position in range(len(text)):

    char = text[position]

    if position % 2 == 0:
        position_type = "Even"
    else:
        position_type = "Odd"

    if char.lower() in "aeiou":
        char_type = "Vowel"
        vowel += 1

    elif char.isalpha():
        char_type = "Consonant"
        consonant += 1

    elif char.isdigit():
        char_type = "Digit"
        digit += 1

    else:
        char_type = "Special character"
        special_character += 1

    print(f"Character: {char} | Position: {position} | "
          f"{position_type} | Type: {char_type}")

print("Vowel:", vowel)
print("Consonant:", consonant)
print("Digit:", digit)
print("Special character:", special_character)

for i in range(1, 6):
    username = input(f"Enter username {i}: ")
    
    length = len(username)
    digit_count = 0
    underscore_count = 0
    has_invalid_char = False
    for char in username:
        if char.isdigit():
            digit_count += 1
        elif char == '_':
            underscore_count += 1
        else:
            has_invalid_char = True
    first_char_valid = length > 0 and (username[0].isalpha() or username[0] == '_')
    if has_invalid_char or length < 5 or length > 15 or not first_char_valid:
        status = "Invalid"
    elif digit_count == 0 or underscore_count == 0:
        status = "Needs Improvement"
    else:
        status = "Valid"
    print(f"\n--- Analysis for '{username}' ---")
    print(f"Length: {length}")
    print(f"First Character Valid: {first_char_valid}")
    print(f"Digits: {digit_count}")
    print(f"Underscores: {underscore_count}")
    print(f"Invalid Special Characters Detected: {has_invalid_char}")
    print(f"Classification: {status}\n")

text=input("Enter a sentence here:")
vowel=0
consonant=0

for position in range(len(text)):
    char=text[position]

    if position %2==0:
        position_type="Even"
    else:
        position_type="Odd"

    if char.lower() in "aeiou":
        char_type="Vowel"
        vowel +=1
    elif char.isalpha():
        char_type="Consonant"
        consonant+=1
    else:
        char_type="Invalid Data"

    if vowel>consonant:
        Score="Vowel Won"
    elif vowel<consonant:
        Score="Consonant Won"
    elif vowel==consonant:
        Score="Draw"
    else:
        Score="Enter valid Data"

print(Score,vowel,consonant,position)

for i in range(1,6):
    units=int(input(f"Enter your electricity Unit here{i}:"))
    if units==100:
        bill=units*5
    elif units>100:
        bill=units*7
    elif units<=200:
        bill=(100*5)+((units-100)*7)
    else:
        bill=(100*5)+(100*7)+((units-100)*15)
    if bill<1000:
        Status=("Low bill")
    elif bill>=3000:
        Status=("Medium bill")
    else:
        Status=("High bill")

    print(f"Your bill is {bill} and your status is {Status}")

