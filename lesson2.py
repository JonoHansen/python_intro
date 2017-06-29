# number guessing game
import random
guessesTaken = 0

myName = raw_input("What's your name >>")
number = random.randint(1, 100)

print "I'm thinking of a number between 1 and 100."

while guessesTaken < 10:
    guess = raw_input("Guess what number")
    guess = int(guess)
    guessesTaken += 1 #this means add 1 to guessesTaken

    if guess < number:
        print "Too low, go higher."
    if guess > number:
        print "Too high, go lower."
    if guess == number:
        break

if guess == number:
    print "Good job %s, you guessed correct in %d turns." % (myName, guessesTaken)
else:
    print "Bad luck, I'm actually thinking of %d." % (number)
