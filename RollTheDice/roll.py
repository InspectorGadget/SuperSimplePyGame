import random

def roll(sides=6):
    num_rolled = random.randint(1, sides)
    return num_rolled


def end():
    print("You ended this game!")


def main():
    rolling = True
    sides = 6
    while rolling:
        roll_again = input("Ready to roll? ENTER = Roll Q = QUIT ")
        if roll_again.lower() != "q":
            num_rolled = roll(sides)
            print("You rolled a", num_rolled)
            end()
        else:
            rolling = False


main()
