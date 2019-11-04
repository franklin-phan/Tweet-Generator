from random import randint



word=input()
sentance=word.split()
for index, word in enumerate(sentance):
    var_random=randint(0,len(sentance)-1)
    sentance[index] = sentance[var_random]

print(sentance)