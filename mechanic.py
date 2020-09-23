import random
from time import sleep as s


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def whats_new():
    print(bcolors.OKBLUE + "Available games:" + bcolors.ENDC)
    print("1. Random numbers.")
    print("2. Paper, rock, scissors")
    x = input("Choose the game:")
    if x == "1":
        random_numbs()
    elif x == "2":
        paper_ect()


def next_of():
    next_choice = input(bcolors.OKBLUE + '\nTo continue press "1", end press "2".\n' + bcolors.ENDC)
    if next_choice == "1":
        whats_new()
    elif next_choice == "2":
        pass
    else:
        pass


def random_numbs():
    number_rand = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print("\nTo win you must guess number between 1 and 9")
    your_choice = input()
    x = random.choice(number_rand)
    s(0.5)
    if your_choice == x:
        print(bcolors.OKGREEN + "Perfect shot." + bcolors.ENDC)
        next_of()
    else:
        print(bcolors.FAIL + "Sorry, but it wasn't a good shot." + bcolors.ENDC)
        print("Right number was: {}".format(x))
        next_of()


def paper_ect():
    comp = ["Paper", "Rock", "Scissor"]

    print("\nIt's a simple game, you must choose between Paper, Rock or Scissor.")
    print("Rules: Scissor > Paper > Rock > Scissor, if there are two same thing it's a row.\n")

    computer_choice = random.choice(comp)
    print(", ".join(comp))
    your_choice = input("Choose your weapon(1, 2 or 3): ")

    if your_choice == "1" and computer_choice == "Rock":
        print("Jeej, you win!")
        next_of()
    elif your_choice == "1" and computer_choice == "Paper":
        print("It's a row.")
        next_of()
    elif your_choice == "1" and computer_choice == "Scissor":
        print("You loose, enemy choose {}.".format(computer_choice))
        next_of()

    if your_choice == "2" and computer_choice == "Scissor":
        print("Jeej, you win!")
        next_of()
    elif your_choice == "2" and computer_choice == "Rock":
        print("It's a row.")
        next_of()
    elif your_choice == "2" and computer_choice == "Paper":
        print("You loose, enemy choose {}.".format(computer_choice))
        next_of()

    if your_choice == "3" and computer_choice == "Paper":
        print("Jeej, you win!")
        next_of()
    elif your_choice == "3" and computer_choice == "Scissor":
        print("It's a row.")
        next_of()
    elif your_choice == "3" and computer_choice == "Rock":
        print("You loose, enemy choose {}.".format(computer_choice))
        next_of()
