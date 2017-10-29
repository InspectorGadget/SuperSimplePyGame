import random

def roll(sides=6):
    num_rolled = random.randint(1, sides)
    return num_rolled


def end():
    print("You ended this game!")


def main():
    Tries = 0
    sides = 6
    rolling = True
    while rolling:
        roll_again = input("Ready to roll again? ENTER = Roll Q = QUIT ")
        if roll_again.lower() != "q":
            num_rolled = int(input("Guess a number: "))
            if num_rolled > roll(6):
                print("You rolled higher, please try again!")
                Tries += 1
                ask = input("You wanna try again? ENTER = Again Q = QUIT ")
                if ask.lower() == "q":
                    end()
                    print("You took " + str(Tries) + " tries!")
                else:
                    main()
            else:
                if num_rolled < roll(6):
                    print("You rolled lower, please try again!")
                    Tries += 1
                    ask = input("You wanna try again? ENTER = Again Q = QUIT ")
                    if ask.lower() == "q":
                        end()
                        print("You took " + str(Tries) + " tries!")
                    else:
                        main()
            if num_rolled == roll(6):
                print("WOAH, you got the right roll! Nice try!")
                Tries += 1
                ask = input("You wanna try again? ENTER = Again Q = QUIT ")
                if ask.lower() == "q":
                    end()
                    print("You took " + str(Tries) + " tries!")
                else:
                    main()
        else:
            rolling = False

    print("Thanks for playing!")


main()
