str1=input("Enter your char1 here: ").upper()
str2=input("Enter your char2 here: ").upper()
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i]==str2[j]:
            print(str1[i],str2[j])