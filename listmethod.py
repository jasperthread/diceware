import random

thephrase = ''

with open('thewords_justwords.txt', 'r') as infile:
    thewords = infile.read().split(', ')

numwords = input('What length of keyphrase would you like?: ')

for num in range(0, int(numwords)):
    randomnumber = random.randint(0, len(thewords))
    thephrase = thephrase + thewords[randomnumber] + ' '

print(thephrase)
