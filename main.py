import random
import printer

foo = ['hello', 'thien', 'dan', 'swillis', 'roxy']
foo = ['hello']
guesses = []
failedAttempts = []
maxAttempts = 6

word = random.choice(foo)

def renderHangman():
    failedAttemptsLength = len(failedAttempts)

    foo = False

    top = '---------------------------'

    print(top)
    print("|" + str(False))
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")

renderHangman()
exit(0)

def isWinner(word, guesses):
    found = True

    # loop through each letter in word and check if that letter has been guessed
    for i in word:
        if i not in guesses:
            found = False

    return found


# the below function will print for "DAN" _A_ if you guessed A
def printWordProgress(word, guesses):
    ret = ''
    for i in word:
        if i in guesses:
            ret = ret + i + ' '
        else:
            ret = ret + '_' + ' '

    return ret


wordLength = len(word)

print('Word: ' + word)

print('You are guessing a word with ' + str(wordLength) + ' characters')

print('You have 5 guesses')

while not isWinner(word, guesses):
    progress = printWordProgress(word, guesses)
    print(progress)

    x = str(input("Please enter a letter: "))
    print('You entered ' + x)


    if x not in word:
        failedAttempts.append(x)

    numberOfFailedAttempts = len(failedAttempts)
    print(str(numberOfFailedAttempts) + ' failed attempts')

    if numberOfFailedAttempts >= maxAttempts:
        break

    guesses.append(x)
    print('Your guesses: ' + ' '.join(guesses))

else:
    print("WINNER")
    print