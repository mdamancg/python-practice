n=input("Enter your char here: ").upper()
for i in range(len(n)):
    count=0
    for j in range(len(n)):
        if n[i]==n[j]:
            count+=1
    if n.find(n[i])==i:
        print(n[i],"=",count)