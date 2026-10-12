choice=int(input("Enter your choice here (1-4):"))
match choice:
    case 1:
        print("Pizza")
    case 2:
        print("Burger")
    case 3:
        print("Pasta")
    case 4:
        print("Sandwich")
    case _:
        print("Invalid choice")

#2
choice=int(input("Enter your choice here (1-5):"))
match choice:
    case 1:
        print("WI-FI")
    case 2:
        print("Bluetooth")
    case 3:
        print("Mobile data")
    case 4:
        print("Airplane mode")
    case 5:
        print("Exit")
    case _:
        print("Invalid Setting")

#3

choice=int(input("Enter your choice (1-5):"))
match choice:
    case 1:
        print("Check Balance")
    case 2:
        print("Withdraw Money")
    case 3:
        print("Deposit Money")
    case 4:
        print("Change pin")
    case 5:
        print("Exit")
    case _:
        print("Invalid choice")

#4
light=input("Enter traffic light here:")
match light:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case _:
        print("Invalid choice")

#5

menu=int(input("Enter your menu number:"))
match menu:
    case 1:
        print("View profile")
    case 2:
        print("View courses")
    case 3:
        print("View marks")
    case 4:
        print("View Attendence")
    case 5:
        print("Logout")
    case _:
        print("Enter choice 1 to 5 sir/mam")

#6

shopping_menu=int(input("Enter your shopping menu number here:"))
match shopping_menu:
    case 1:
        print("Electronics")
    case 2:
        print("Clothing")
    case 3:
        print("Books")
    case 4:
        print("Grocery")
    case 5:
        print("Exit")
    case _:
        print("Enter valid choice here!!!!!!")

#7
application=int(input("Enter your choice here:"))
match application:
    case 1:
        print("Account Balance")
    case 2:
        print("Mini statement")
    case 3:
        print("Fund Transfer")
    case 4:
        print("Bill Payment")
    case 5:
        print("Customer Support")
    case _:
        print("Enter valid input")

#8
Booking=int(input("Enter your choice here:"))
match Booking:
    case 1:
        print("Morning show")
    case 2:
        print("Afternoon Show")
    case 3:
        print("Evening show")
    case 4:
        print("Night Show")
    case _:
        print("Enter valid input")

#9
whether=int(input("Enter whether here:"))
print("1-Sunny 2-Rainy 3-Cloudy 4-Snowy")

match whether:
    case 1:
        print("Wear sunglasses")
    case 2:
        print("Carry an umbrella")
    case 3:
        print("Weather may change")
    case 4:
        print("Wear warm clothes")
    case _:
        print("Unknown Weather")

#10
payment = input("Enter your payment method:")
match payment:
    case "upi":
        print("UPI payment selected")
    case "card":
        print("Card payment selected")
    case "cash":
        print("Cash payment selected")
    case "Wallet":
        print("Wallet payment selected")
    case _:
        print("Invalid payment method")

#11
extension = input("Enter Extension:").lower()
match extension:
    case "Pdf":
        print("Document type:",extension)
    case "jpg":
        print("Document type:",extension)
    case "png":
        print("Document type:",extension)
    case "mp3":
        print("Document type:",extension)
    case "mp4":
        print("Document type:",extension)
    case _:
        print("Unknown file selected")

    #12

role=input("Enter your role here:").lower()
match role:
    case "admin":
        print("Full access")
    case "teacher":
        print("Teacher Dashboard")
    case "student":
        print("Student Dashboard")
    case "guest":
        print("Limited access")
    case _:
        print("Invalid role!!!!!!!!!!!")
                 #Topic-4
#13

day=int(input("Enter your day here:"))
print('''1 → Monday
2 → Tuesday
3 → Wednesday
4 → Thursday
5 → Friday
6 → Saturday
7 → Sunday''')
match day:
    case 1|2|3|4|5:
        print("Weekday!!!")
    case 6|7:
        print("Weekend!!")
    case _:
        print("Invalid day")

#14
print('''1 → Low
2 → Medium
3 → High
4 → Critical''')
system=int(input("Enter your Support Here: "))
match system:
    case 1|2:
        print("Normal Priority")
    case 3|4:
        print("Urgent Priority")
    case _:
        print("Lundi")

#15
print('''1 → Bronze
2 → Silver
3 → Gold
4 → Platinum''')
membership=int(input("Enter your Membership type number here:"))
match membership:
    case 1|2:
        print("Basic Membership!!!")
    case 3|4:
        print("Premium Membership")
    case _:
        print("Enter your valid membership here!!!")

#               Topic 5 — Nested match-case

#16

account="student"
choice=2
match account:
    case "student":
        match choice:
            case 1:
                print("View courses!!")
            case 2:
                print("View marks!!")
            case 3:
                print("View Attendance!!!")
            case _:
                print("Invalid choice!!!!")

    case "teacher":
        match  choice:
            case 1:
                print("View Students")
            case 2:
                print("Enter marks")
            case _:
                print("Invalid choice!!!")

    case _:
        print("Invalid Account Type")

#17
bank=input("Enter your bank type saving or current:")
option=int(input("Enter your option here: "))

match bank:
    case "saving":
        match option:
            case 1:
                print("Selected check balance!!!!")
            case 2:
                print("Deposit selected!!")
            case 3:
                print("Withdraw Selected")
            case _:
                print("Enter valid choice!!!")
    case "current":
        match option:
                    case 1:
                        print("Selected check balance!!!!")
                    case 2:
                        print("Deposit selected!!")
                    case 3:
                        print("Withdraw Selected")
                    case _:
                        print("Enter valid choice!!!")
    case _:
        print("Enter valid Account type here !!!!")

#18

category=input("Enter category type here electronics or clothing: ").lower()
option=int(input("Enter your option 1-3 :"))

match category:
    case "electronics":
        match option:
            case 1:
                print("Mobile Selected!!")
            case 2:
                print("Laptop selected!!!")
            case 3:
                print("Headphone selected!!!!")
            case _:
                print("Enter valid options!!")
    case "clothing":
        match option:
            case 1:
                print("Shirt Selected!!")
            case 2:
                print("Jeans Selected!!")
            case 3:
                print("Shoes selected!!!")
            case _:
                print("Enter valid options !!!!")
    case _:
        print("Enter valid category")

#19
category=input("Enter Your type veg or non-veg:")
option=int(input("Enter your option here 1-3: "))

match category:
    case "veg":
        match option:
            case 1:
                print("Paneer Selected!!")
            case 2:
                print("Dal selected!!")
            case 3:
                print("Veg Biryani!!!")
            case _:
                print("Enter valid options!1")
    case "non veg":
        match option:
            case 1:
                print("Chicken Biryani selected!!")
            case 2:
                print("Chicken Curry Selected!!")
            case 3:
                print("Fish Fry Selected!!!")
            case _:
                print("Enter valid option!!!")
    case _:
        print("Please Enter Valid choice here!!!")

#20

number1=0
number2=0
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus")
value=1

while value != 0:
    number1 = int(input("Enter number1:"))
    number2 = int(input("Enter number2:"))
    value = int(input("Enter your choice (1-5):"))
    if value == 0:
        print("Exiting...")
        break
    match value:
        case 1:
            print("Addition:", number1 + number2)
        case 2:
            print("Subtraction:", number1 - number2)
        case 3:
            print("Multiplication:", number1 * number2)
        case 4:
            print("Division:", number1 / number2)
            if number2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print("Division:", number1 / number2)
        case 5:
            print("Modulus:", number1 % number2)
        case _:
            print("Invalid choice")

#method2

num1=int(input("Enter your number here: "))
num2=int(input("Enter your number 2 here: "))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus")
operator=int(input("Enter your Operator Type:"))

match operator:
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1 * num2)
    case 4:
        print(num1/num2)
    case 5:
        print(num1%num2)
    case _:
        print("Enter valid operator here!!!")

#21

choice = int(input("Enter choice: "))
temperature = float(input("Enter temperature: "))

if choice == 1:
    fahrenheit = (temperature * 9 / 5) + 32
    print("Temperature =", fahrenheit, "F")

elif choice == 2:
    celsius = (temperature - 32) * 5 / 9
    print("Temperature =", celsius, "C")

else:
    print("Invalid choice")

#Q22]      

print("1 ==> Kilometers to meters \n 2==> Meters to Kilometers \n 3==> Kilograms to Grams \n 4==> Grams to Kilograms") 

choice=int(input("Enter your choice number:-")) 
num=int(input("Enter your value:-"))

match choice:
    case 1:
        meters = num*1000 
        print(f"{num} kms  is equal to {meters} meters") 
    case 2:
        kilometers=num/1000
        print(f"{num} meters is equal to {kilometers} kms") 
    case 3:
        grams=num*1000
        print(f"{num} kilograms is equal to {grams} grams.")
    case 4:
        kilograms=num/1000
        print(f"{num} grams is equal to {kilograms} kgs.") 
    case _:
        print("Invalid choice number") 



# Q23] 

Account_type=input("Enter your account type:-").strip().lower() 
amount=int(input("Enter your amount:-"))

match Account_type:
    case "savings": 
        if amount>0:
            print("Withdrawal Request Accepted") 
        else:
            print("Invalid amount") 
    case "current":
        if amount>0:
            print("Withdrawal request Accepted")
        else:
            print("Invalid Amount") 
    case _:
        print("Invalid CAccount Type")




# Q24] 

print(" 1 ==> Start Exam \n 2==> View Result \n 3 ==> Exit")
choice=int(input("Enter your choice Number:-"))
age=int(input("Enter your age:-"))

match choice:
    case 1:
        if age>=18:
            print("You can start the exam")
        else:
            print("You are under threshold age")
    case 2:
        print("You can see your result")
    case 3:
        print("Exam ended")
    case _:
        print("Invalid choice number")               
    


# Q25]
print(" 1 ==> Regular \n 2 ==> Premium \n 3 ==> VIP  ")

ticket_type = int(input("Enter ticket type: "))
age = int(input("Enter your age: "))
match ticket_type:
    case 1:
        if age<=5:
         print("Free Ticket")
        else:
            print("Your selected ticket type is ", ticket_type)
    case 2:
        if age<=5:
            print("Free Ticket")
        else:
            print("Your selected ticket type is ", ticket_type)
    case 3:
         if age<=5:
                     print("Free Ticket")
         else:
                     print("Your selected ticket type is ", ticket_type)
    case _:
       print("Invalid ticket type") 



# Q26]

print("1 → Light\n2 → Fan\n3 → AC\n4 → TV")

choice = int(input("Enter device: "))

match choice:
    case 1:
        print("Light Controller Opened")
    case 2:
        print("Fan Controller Opened")
    case 3:
        print("AC Controller Opened")
    case 4:
        print("TV Controller Opened")
    case _:
        print("Invalid Device")



# Q27]

print("1 → General Medicine\n2 → Cardiology\n3 → Orthopedics\n4 → Pediatrics\n5 → Emergency")

choice = int(input("Enter department: "))

match choice:
    case 1:
        print("General Medicine Selected")
    case 2:
        print("Cardiology Selected")
    case 3:
        print("Orthopedics Selected")
    case 4:
        print("Pediatrics Selected")
    case 5:
        print("Emergency Selected")
    case _:
        print("Invalid Department")


# Q28]

print("1 → Book Ticket\n2 → Cancel Ticket\n3 → Check PNR\n4 → Train Schedule\n5 → Exit")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Book Ticket Selected")
    case 2:
        print("Cancel Ticket Selected")
    case 3:
        print("Check PNR Selected")
    case 4:
        print("Train Schedule Selected")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")


# Q29]

print("1 → Search Book\n2 → Issue Book\n3 → Return Book\n4 → View Issued Books\n5 → Exit")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Search Book Selected")
    case 2:
        print("Issue Book Selected")
    case 3:
        print("Return Book Selected")
    case 4:
        print("View Issued Books Selected")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")



# Q30]

print("placed\nconfirmed\npreparing\nout_for_delivery\ndelivered\ncancelled")

status = input("Enter status: ").strip().lower()

match status:
    case "placed":
        print("Your order has been placed")
    case "confirmed":
        print("Your order has been confirmed")
    case "preparing":
        print("Your order is being prepared")
    case "out_for_delivery":
        print("Your order is on the way")
    case "delivered":
        print("Your order has been delivered")
    case "cancelled":
        print("Your order has been cancelled")
    case _:
        print("Invalid Order Status")


# Q31]

print("1 → Personal Banking\n2 → Business Banking")

banking_type = int(input("Enter banking type: "))

match banking_type:

    case 1:
        print("1 → Balance\n2 → Transfer\n3 → Loan")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Personal Banking - Balance Selected")
            case 2:
                print("Personal Banking - Transfer Selected")
            case 3:
                print("Personal Banking - Loan Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("1 → Balance\n2 → Payroll\n3 → Business Loan")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Business Banking - Balance Selected")
            case 2:
                print("Business Banking - Payroll Selected")
            case 3:
                print("Business Loan Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Banking Type")


# 32]

print("1 → Student\n2 → Teacher\n3 → Parent")

role = int(input("Enter role: "))

match role:

    case 1:
        print("1 → Marks\n2 → Attendance\n3 → Homework")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Student Marks Selected")
            case 2:
                print("Student Attendance Selected")
            case 3:
                print("Student Homework Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("1 → Enter Marks\n2 → Attendance\n3 → Assign Homework")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Enter Marks Selected")
            case 2:
                print("Teacher Attendance Selected")
            case 3:
                print("Assign Homework Selected")
            case _:
                print("Invalid Option")

    case 3:
        print("1 → Child Marks\n2 → Child Attendance\n3 → Contact Teacher")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Child Marks Selected")
            case 2:
                print("Child Attendance Selected")
            case 3:
                print("Contact Teacher Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Role")



# 33]

print("1 → Flight\n2 → Train\n3 → Bus")

transport = int(input("Enter transport: "))

match transport:

    case 1:
        print("1 → Economy\n2 → Business")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Economy Selected")
            case 2:
                print("Business Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("1 → Sleeper\n2 → AC")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Sleeper Selected")
            case 2:
                print("AC Selected")
            case _:
                print("Invalid Option")

    case 3:
        print("1 → Ordinary\n2 → Volvo")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Ordinary Selected")
            case 2:
                print("Volvo Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Transport")


# Q 34]

print("1 → Start Game\n2 → Load Game\n3 → Settings\n4 → Exit")

choice = int(input("Enter choice: "))

match choice:

    case 1:
        print("Game Started")

    case 2:
        print("Game Loaded")

    case 3:
        print("1 → Sound\n2 → Graphics\n3 → Controls")
        option = int(input("Enter setting: "))

        match option:
            case 1:
                print("Sound Settings Opened")
            case 2:
                print("Graphics Settings Opened")
            case 3:
                print("Controls Settings Opened")
            case _:
                print("Invalid Setting")

    case 4:
        print("Exit")

    case _:
        print("Invalid Choice")
