import random

with open('thewords.txt', 'r') as infilehandle:
    wordage = infilehandle.read().split(' ')

thedict = {}
num = 0
while num in range(0, len(wordage)):
    # build key + value pairs
    thedict[wordage[num]] = wordage[num + 1]
    num += 2

print("""Based on the diceware concept of passkey generation.
The greater the length of the passphrase, the increase in exponential
difficulty in cracking it. 7+ words would take ten years or more to crack.\n
For more information: https://theintercept.com/2015/03/26/passphrases-can-memorize-attackers-cant-guess/\n""")

numpicks = input('How many words would you like for this passphrase?: ')

iter = 0
phrase = ''
numbercombos = []
while iter < int(numpicks):
    aninteger = str(random.randint(11111, 66666))
    try:
        phrase = phrase + thedict[aninteger] + ' '
        numbercombos.append(aninteger)
        iter += 1
    except:
        pass

print('Your phrase is:', phrase, '\nUsing the numbers:', numbercombos)
