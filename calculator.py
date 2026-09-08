print("1.Add","2.SUB","3.Multiple","4.Div","5.Float division")
number=int(input("Enter your number to find result:"))
num1=float(input("Enter your number1:"))
numb2=float(input("Enter your number2:"))

if number==1:
    print(num1+numb2)
elif number==2:
    print(num1-numb2)
elif number==3:
    print(num1*numb2)
elif number==4:
    print(num1/numb2)
elif number==5:
    print(num1//numb2)
else:
    print("Enter valid number.")
