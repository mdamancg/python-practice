n=input("Enter your char here: ").upper()
for i in range(len(n)):
    for j in range(len(n)):
        if ord(n[i])<ord(n[j]):
            print(n[i],n[j],"->","Increasing")
        elif ord(n[i])>ord(n[j]):
            print(n[i],n[j],"->","Decreasing")
        elif ord(n[i])==ord(n[j]):
            print(n[i],n[j],"->","Same")
        else:
            print("Enter right plz !!!!!")