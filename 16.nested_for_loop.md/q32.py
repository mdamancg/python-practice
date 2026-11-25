n=input("Enter your character here: ").upper()
for i in range(len(n)):
    for j in range(len(n)):
        if n[i] in "AEIOU" and n[j] not in "AEIOU":
            print(n[i],n[j])