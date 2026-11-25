n=input("Enter your character here: ")
for i in range(len(n)):
    # for j in range(len(n)):
        if n[i] in "aeiouAEIOU":
            print(n[i], "=", "Vowel")
        else:
            print(n[i],"=","Consonant")