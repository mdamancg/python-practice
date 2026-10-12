#1) 1 2 3 4 finished
#2) s k y l
#3) 2 4 6

#      A2. Write a Program --- Medium

# for i in range(1,10):
#     if i==7:
#         break
#     print(i,end=" ")

# str = "computer"
# count = 0
# for ch in str:
#     if ch == "p":
#         count += 1
#         break
# print("Found", count)

# numbers = [4, 8, 2, -3, 9]

# for number in numbers:
#     if number < 0:
#         break

#     print(number)

# word=input("Enter your word here: ").lower()
# for ch in word:
#     if ch=="p":
#      print("Found")
#      break
# else:
#    print("Not found")

#            Section B --- Practice Problems on continue

# for i in range(1, 7):
#     if i == 4:
#         continue
#     print(i)

# for ch in "education":
#     if ch in "aeiou":
#         continue
#     print(ch, end="")

# n = 0

# while n < 5:
#     n += 1
#     if n == 3:
#         continue
#     print(n)

# num=int(input("Enter your number here: "))
# for i in range(1,num+1):
#     if i%3==0:
#         continue
#     print(i)


# text = input("Enter your string: ")
# char = input("Enter character to remove: ")

# for ch in text:
#     if ch == char:
#         continue
#     print(ch, end="")


# marks = input("Enter marks separated by spaces: ").split()

# for mark in marks:
#     mark = int(mark)

#     if mark < 40:
#         continue

#     print(mark, end=" ")


#        B3. Think Carefully --- Challenging

# n=1
# while n<=5:
#     if n==3:
#         n+=1
#         continue
#     print(n)
#     n+=1

# str = input("Enter your word here: ").lower()
# for ch in str:
#     if ch in "aeiou":
#         continue
#     print(ch, end=" ")

#      Section C --- Practice Problems on for-else

# for i in range(1, 4):
#     print(i)
# else:
#     print("Done")

# for i in range(1, 5):
#     if i == 2:
#         continue
#     print(i)
# else:
#     print("Completed")

# for i in range(1, 5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Completed")
# print("Outside loop")

#          C2. Write a Program --- Medium

# marks = input("Enter marks separated by spaces: ").split()
# option = int(input("Enter your option you want to find: "))
# count = 0
# for mark in marks:
#     mark = int(mark)
#     if mark == option:
#         count += 1
#         print("Found", count)
#         break
# else:
#     print("Not found!!!")


# text = input("Enter your string: ").lower()
# char = input("Enter character you want to find: ").lower()

# for ch in text:
#     if ch == char:
#         print("Character exists")
#         break
# else:
#     print("Character missing")


# num=int(input("Enter your number here: "))
# count=0
# for i in range(2,num-1):
#     count+=1
#     if num%i==0:
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime!!!!")

# print(count)

#         C3. Think Carefully --- Challenging

# values = [2, 4, 6, 8]

# for value in values:
#     if value % 2 != 0:
#         print("Odd found")
#         break
# else:
#     print("All are even")

#            C3. Think Carefully --- Challenging

# values = [2, 4, 6, 8]
# for value in values:
#     if value % 2 != 0:
#         print("Odd found")
#         break
# else:
#     print("All are even")

# for x in range(3):
#     continue
# else:
#     print("A")

# for x in range(3):
#     break
# else:
#     print("B")

# for x in range(0):
#     print(x)
# else:
#     print("C")

# s=input("Enter a string: ").lower()
# for ch in s:
#     if s.count(ch)>=2:
#         print(ch)
#         break
# else:
#     print("No repeated character")

#      Section D --- Practice Problems on pass

# for i in range(1, 4):
#     if i == 2:
#         pass
#     print(i)

# x=10
# if x>10:
#     pass
# print("Finished")

# for letter in "cat":
#     pass
# print("Loop ended!!")

#          D2. Write a Program --- Medium


# for i in range(1, 6):
#     if i % 2 == 0:
#         pass
#     print(i)

# choice = int(input("Enter your choice (1 or 2): "))

# if choice == 1:
#     print("Welcome to the program")
# elif choice == 2:
#     pass
# else:
#     print("Invalid choice")

# print("Program closed")


#        D3. Think Carefully --- Challenging

# for i in range(1, 5):
#     if i == 3:
#         pass
#     print(i)

# for i in range(1, 5):
#     if i == 3:
#         continue
#     print(i)

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

#       Section E --- Mixed Challenge Questions

# for i in range(1,4):
#     if i==2:
#         continue
#     if i==4:
#         break
#     print(i)
# else:
#     print("Finished!!!!")

# numbers = [-2, 4, 7, 9]
# target = 7

# for num in numbers:
#     if num < 0:
#         continue

#     if num == target:
#         print("Target found")
#         break
# else:
#     print("Target not found")

# numbers = [2, 0, 4, -1, 8]

# for num in numbers:
#     if num == 0:
#         continue

#     if num == -1:
#         break

#     print(num)
# else:
#     print("All values processed")

# for i in range(1, 4):
#     for j in range(1, 3):
#         print(i, j)



# for row in range(1,4):
#     for col in range(1,4):
#         if col ==2:
#             continue
#         if row==3:
#             break
#         print(row,col)
#     else:
#         print("Inner loop completed!!!!!")



numbers = [-8, -3, 5, 12, 18, 24, 36]

# for num in numbers:
#     if num < 0:
#         continue

#     if num % 4 == 0 and num % 6 == 0:
#         print("First matching number:", num)
#         break
# else:
#     print("No matching number found")
