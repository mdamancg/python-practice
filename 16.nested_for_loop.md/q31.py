n = input("Enter your characters here: ").upper()
for i in range(len(n)):
    for j in range(len(n)):
        if n[i] == n[j]:
            print(n[i] + "/" + n[j], "is Same", end="; ")
        else:
            print(n[i] + "/" + n[j], "is Different", end="; ")
    print()
