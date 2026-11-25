# str1=input("Enter your char1 here: ")
# str2=input("Enter your char2 here: ")
# for i in range(len(str1)):
#     for j in range(len(str2)):
#         if str1[i]==str2[j]:
#             print(f"Common character include {str1[i]} and {str2[j]}")


str1 = input("Enter your char1 here: ").upper()
str2 = input("Enter your char2 here: ").upper()
for i in range(len(str1)):
    if str1[i] in str2 and str1.find(str1[i]) == i:
        print(f"Common character: {str1[i]}")
