sentence=input("Enter your char here: ")
words=sentence.split()
for i in range (len(words)):
    for j in range(len(words)):
     print(words[i],words[j])