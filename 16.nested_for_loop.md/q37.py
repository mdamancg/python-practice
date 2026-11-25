# sentence=input("Enter your char here: ")
# words=sentence.split()
# for i in range (len(words)):
#     for j in range(len(words)):
#      if i==j:
#         print(words[i],words[j])

sentence=input("Enter your char here: ")
words=sentence.split()
for i in range(len(words)):
    for j in range(len(words)):
        if len(words[i])==len(words[j]) and i<j:
            print(words[i],words[j])