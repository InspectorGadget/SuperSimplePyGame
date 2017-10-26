import random


def onrun():

    number = random.randint(0, 10000000000000000000000000000000000000000000000)
    tries = int(1)

    question = input("Would you like to play a game? [Y/N]")

    if question.lower() == "n":
        print("Oh, it's okay. Byeee")
    if question.lower() == "y":
        print("Can you guess a number? ")
        guess = int(input("Have a guess: "))
        if guess <= number:
            print("Guess Lower, try again! :D")
            again = input("Wanna try again? [Y/N]")
            if again.lower() == "y":
                print("Sure, starting now...")
                onrun()
            else:
                if again.lower() == "n":
                    print("You ended this game with " + str(tries) + " tries!")
        if guess >= number:
            print("Guess Higher, try again! :D")
            again = input("Wanna try again? [Y/N]")
            if again.lower() == "y":
                print("Sure, starting now...")
                onrun()
            else:
                if again.lower() == "n":
                    print("You ended this game with " + str(tries) + " tries!")
        if guess == number:
            print("Oops, you actually guessed correctly!")
            print("---GAME OVER---")
        if guess == "0":
            print("You made a foul by entering " + guess + ", so start again!")
            ask = input("You wanna start again? ")
            if ask.lower() == "y":
                onrun()
            else:
                if ask.lower() == "n":
                    print("Okay, bye!")
                    print("You ended this game with " + str(tries) + " tries!")


print("Welcome to InspectorGadget's Python Game!")
username = input("Hello! What is your username? ")
print("Welcome, " + username + "!")

onrun()
