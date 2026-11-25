n=input("Enter your char here: ")
for i in range(len(n)):
    for j in range(len(n)):
        if n[i].isupper() and n[j].isupper():
            print(n[i],n[j])
        elif n[i].islower() and n[j].islower():
            print(n[i],n[j])