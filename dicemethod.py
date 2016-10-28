with open('thewords.txt', 'r') as infilehandle:
    wordage = infilehandle.read().split(' ')

num = 0

loopit = True

thedict = {}

thephrase = ''

while num in range(0, len(wordage)):
    # build key + value pairs
    thedict[wordage[num]] = wordage[num + 1]
    num += 2

print('Based on the diceware concept of passkey generation.\nRoll a six-sided die 5 times and record each number\n'
      'as a 5 digit group like \"62146.\"'
      '\n\nEnter the number below to generate a random word. '
      'When you are done, you will have a generated passphrase.'
      '\n\nDo it 7 times and even the Chinese can\'t crack it.\n\nFor more '
      'information: https://theintercept.com/2015/03/26/passphrases-can-memorize-attackers-cant-guess/\n\n')

while loopit == True:
    diced = input('Enter your digits. Enter \"Done\" when you are done: ')
    if diced == 'Done':
        break
    else:
        try:
            thephrase = thephrase + thedict[diced] + ' '
        except:
            print('@@@ Roll another number. That one is not on the list. @@@\n')

print('Here is your phrase. Write it down. Memorize it. Burn it.' + '\n' + thephrase)

# print(thedict)