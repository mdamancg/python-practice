n=input("Enter your character here: ").upper()

for i in range(len(n)):
    for j in range(len(n)):
        if i !=j:
            print(n[i],n[j],end=",")