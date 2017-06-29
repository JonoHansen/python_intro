from sys import exit

#declare a function called "start" and print out 3 lines of story
def start():
    print "You just woke up in a small room with no memory of how you got there, you have nothing but your clothes and your wallet."
    print " There is a sewer door and a ladder leading up to an attic. "

    while True:
        print "Which way will you choose? >> "
        choice = raw_input("sewer door / attic >>")

        #Write a conditinal that calls bear_room() if we go to the left, and cthulhu_room() if we go right.
        if choice == "sewer door":
            crocodile_room()
        elif choice == "attic":
            oldlady_room()
        else:
            print "you sat there doing nothing for 15 minutes, before realizing you might die of starvation if you don't do anything."

def crocodile_room():
    print "You enter the sewer, behind you is a wall so you can only exit in one direction."
    print "There's a crocodile in front of you in the sewer."
    print "He's just sitting in the middle of the sewer."
    print "How are you going to get around the crocodile? >>"
    crocodile_moved = False
    while True:
        choice = raw_input("step over it / kindly ask it to move / distract it with your wallet >>")
        if choice == "step over it":
            dead("The crocodile bites you and rips you in half. Game over.")
        if choice == "distract it with your wallet":
            dead("The crocodile morphs into a mysteries figure who grabs your wallet, finding nothing but 4 1 dollar bills, he stuffs all the bills in your mouth, choking you to death. Game over.")
        elif choice == "kindly ask it to move" and not crocodile_moved:
            print "The crocodile kindly moves a step backwards, not changing a thing."
            crocodile_moved = True
        elif choice == "kindly ask it to move" and crocodile_moved:
            dead("The crocodile is affended by you asking him to move twice and rips of your face. Game over")
        elif choice == "step over it" and crocodile_moved:
            print "The crocodile realizes you wanted him to move so you could pass it, and laughs it off."
            cash_room()
        elif choice == "distract it with you wallet" and crocodile_moved:
            dead("Totally confused, he leaves, but as you keep going down the sewer  he comes back with papa croc, and papa rips you into little pieces. Game over.")

def cash_room():
    print "You walk to the end of a sewer , and find a door with an ATM attached to it."
    print "On the ATM, there is a sign that says a certain amount of money is required to open the door."
    print "You open your wallet, and find 22 dollars and your debit card"
    print "What do you do?"
    choice = raw_input("put your 22 dollars into the ATM / put your debit card into the ATM >>")
    if choice == "put your 22 dollars into the ATM":
        dead("the machine unsatified with the amount of money you have, blows up, and fries you into a crispy snack for the hungry crocodile. Game over.")
    if choice == "put debit card into the ATM":
        print "The machine asks tells you it needs 10000 dollars to open the door."
        print "How much will you deposit?"
        deposit_moved = False
        while True:
            choice = int(raw_input("Write a number:  "))

            if choice > 10000:
                print "The ATM tells you 'Insufficient funds, please deposit 10000'."
                deposit_moved = True
                if choice > 10000 and deposit_moved:

                    if choice <= 10000:
                        dead ("The ATM tells you 'Haha! you just got scammed!' Suddenly a group of crocodiles attack you, ripping you to pieces. Game over.")

def oldlady_room():
    print "You climb up to the attic, and there is an old lady sitting in a chair with her back facing you."
    print "She tells you that if you answer her riddle correctly, she will tell you how to escape, if not, you will die."
    print "What do you do? >>"
    choice = raw_input("answer her riddle / leave the attic >>")
    if choice == "leave the attic":
        print "You left the attic, afraid that you will answer her riddle incorrectly."
    if choice == "answer her riddle":
        print "The lady first tells you that you have the freedom to answer with your own opinion, and your opinion is usually correct. Then she says 'you are in at a park, you are trying to make some money, would you ask a hobo, a child, or a drunk man?' "
        choice = raw_input("a hobo / a baby / a drunk man / or something else? >>")
    if "a merchant" in choice or "a bartender" in choice or "a drunk man" in choice:
        dead("She tells you this is a horrible answer. Then she turns around and shoots you in the face. Game over")
    elif choice == "none of them":
        print "she tells you that you are correct, and to escape the house, all you have to do is hit that button."
        print "Do you hit the button?"
        choice = raw_input("yes / no >>")
        if choice == "yes":
            print("the entire house explodes, you corpse gets flung out of the house, technically, you escaped, but you died. Win or lose, you decide.")
        if choice == "no":
            print "she says, 'suit yourself.' and with a snap, you are knocked out."
        start()

def dead(msg):
    print msg
start()

# Write a while loop that repeats forever unless we run dead() or gold_room(). There will be three options.
