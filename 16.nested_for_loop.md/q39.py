sentence=input("Enter your char here: ")
words=sentence.split()
for i in range(len(words)):
    for j in range(len(words)):
        if words[i][-1]==words[j][-1]:
            print(words[i],words[j])