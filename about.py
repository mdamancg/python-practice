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

sum=0
for i in range (1,100):
    sum=sum+i
    average=sum/99
    print(average)

number=int(input("Enter your number:"))
for i in range(number):
    if i%2==0:
        print(f"{i}number is even")