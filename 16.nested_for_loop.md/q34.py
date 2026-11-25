n=input("Enter your char here: ").upper()
for i in range(len(n)):
    for j in range(len(n)):
        if i !=j:
            diff=abs(ord(n[i])-ord(n[j]))
            print(n[i],n[j],"->",diff)