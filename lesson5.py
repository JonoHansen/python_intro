import random

HANGMANPICS = ['''
 +---+
 |   |
     |
     |
     |
     |
=========''','''
 +---+
 |   |
 O   |
     |
     |
     |
=========''','''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========''','''
 +---+
 |   |
 O   |
 |\  |
     |
     |
=========''','''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''','''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''','''
 +---+
 |   |
 O   |
/|\  |
/ \   |
     |
=========''']

#method showing the picture, the incorrect guesses and current blanks
def displayBoard(HANGMANPICS, missedLetters, correctLetters, myWord):
    print(HANGMANPICS[len(missedLetters)])
    print("You've taken %d incorrect guesses." % len(missedLetters))
    #loop to print out all incorrect guesses
    for letter in missedLetters:
        print(letter)
    #variable to hold blanks
    blanks = '_' * len(myWord)
    #prints out any correct guesses inside our blanks
    for i in range(len(myWord)):
        if myWord[i] in correctLetters:
            blanks = blanks[:i] + myWord[i] + blanks[i+1:]
    print blanks

#method to get the user's input (the actual guessing of the letter)
def getGuess(alreadyGuessedLetters):
    while True:
        guess = raw_input("Guess a letter!")
        guess = guess.lower()
        if len(guess) != 1:
            print("Please guess one letter :S")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a letter >.<")
        elif guess in alreadyGuessedLetters:
            print("You already guessed that letter! >:( ")
        else:
            return guess

#method to generate a random word
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList.split()) - 1)
    return wordList.split()[wordIndex]

#setting up variables as inputs
#Set up game variables and inputs
words = "kidding silly phone fantastic pokemon blizzard weapon calling singer articulate stupidity question tissue sushi suicide reposition instant flashback dual impossible unforgetable indupitably index zebra reflexes reflecting china chimichanga"
print "Let's play hangman!"
myWord = getRandomWord(words)
gameOver = False
correctLetters = ""
missedLetters = ""

# Main loop for game
while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters , myWord)
    guess = getGuess(correctLetters + missedLetters)
    # check if the user  guess is correct
    if guess in myWord:
        correctLetters = correctLetters + guess
        # check for whether the player has won
        win = True
        for i in range(len(myWord)):
            if myWord[i] not in correctLetters:
                win = False
                break
            if win:
                print "You win!"
                gameOver = True
    else:
        missedLetters = missedLetters + guess
        # check for loss
        if len(missedLetters) == len(HANGMANPICS)-1:
            displayBoard (HANGMANPICS, missedLetters, correctLetters, myWord)
            print "You lost! The word is %s" % myWord
            gameOver = True
    if gameOver:
        answer = raw_input("Do you want to play again? yes / no >>")
        answer.lower()
        if "yes" in answer:
            myWord = getRandomWord(words)
            gameOver = False
            correctLetters = ""
            missedLetters = ""
        else:
            break
