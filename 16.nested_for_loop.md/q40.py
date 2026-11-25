# sentence=input("Enter your char here: ")
# words=sentence.split()
# for i in range(len(words)):
#     for j in range(len(words)):
#      if words[i]==words[j]:
#       print("Matched word pairs")
#     #  else:
#     #    print("Enter valid!!")
# # print()

sentence = input("Enter your sentence here: ")
words = sentence.split()
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        for ch in words[i]:
            if ch in words[j]:
                print(words[i], words[j])
                break