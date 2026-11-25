#                                         Beginner

#1
def function():
    city="Delhi"
    print(city)
function()

#2
school="ABC"
def function():
    global school
    school="DEF"
    print(school)
function()

#3

def function():
    if True:
        result=25
        print(result)
function()

#4
for number in range(4):
    pass
print(number)

#5
# scope:Scope defines where a variable can be accesssed or used in the code.
#Lifetime: Lifetime defines how long a variable exists in memory during program execution.

#              Intermediate

#6
value = 100
def test():
    value = 200
    print(value)
test()  #200
print(value) #100

#7
clicks=0
def click():
    global clicks
    clicks+=1
click()
print(clicks)

#8
name = "Asha"
def show():
    print(name)
    name = "Ravi"
show() # UnboundedLocalError aayega kyuki name="Ravi" bounded nhi hai function se.

#9

name="Aman"
def outer():
    name="MD"
    def inner():
        print(name)
    inner()
outer()

#10
def get_number():
    numbers=[10,20,30]
    return numbers
result=get_number()
print("Original list:",result)
result.append(40)
result[0]=100
print("Modified Result:",result)

#                       Challenging
#11

def outer():
    count=0
    def increment():
        nonlocal count
        count=count+1
        return count
    return increment
counter=outer()
print(counter())
print(counter())
print(counter())

#12

x = 1
def outer():
    x = 2
    def inner():
        x = 3
        print(x)
    inner() #3
    print(x) #2
outer() 
print(x) #1

