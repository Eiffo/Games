import random
from time import sleep as s

# class to color words
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Main menu; every available game
def whats_new():
    print(bcolors.OKBLUE + "Available games:" + bcolors.ENDC)
    print("1. Random numbers.")
    print("2. Paper, rock, scissors")
    x = input("Choose the game:")
    if x == "1":
        random_numbs()
    elif x == "2":
        paper_ect()
    else:
        print("Sorry, we don't have that game!")

# kind of loop to play again and again without reopen program
def next_of():
    next_choice = input(bcolors.OKBLUE + '\nTo continue press "1", end press "2".\n' + bcolors.ENDC)
    if next_choice == "1":
        whats_new()
    elif next_choice == "2":
        pass
    else:
        pass

# Game to guess correct number
def random_numbs():
    number_rand = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print("\nTo win you must guess number between 1 and 9")
    your_choice = input()
    x = random.choice(number_rand)
    s(0.5) # Sleep for half sec
    if your_choice == x:
        print(bcolors.OKGREEN + "Perfect shot." + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "Sorry, but it wasn't a good shot." + bcolors.ENDC)
        print("Right number was: {}".format(x))
    next_of()

# Game for Paper, Rock, Scissor
def paper_ect():
    comp = ["Paper", "Rock", "Scissor"]

    print("\nIt's a simple game, you must choose between Paper, Rock or Scissor.")
    print("Rules: Scissor > Paper > Rock > Scissor, if there are two same thing it's a row.\n")

    computer_choice = random.choice(comp) # generate "random" number
    print(", ".join(comp))
    your_choice = input('Choose your "weapon"(1, 2 or 3): ')
    print("\n")

    # Mechanism to find winner
    if your_choice == "1" and computer_choice == "Rock":
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        print("Enemy choose {}.".format(computer_choice))
        next_of()
    elif your_choice == "1" and computer_choice == "Paper":
        print("It's a row. Enemy choose {}.".format(computer_choice))
        next_of()
    elif your_choice == "1" and computer_choice == "Scissor":
        print("You loose, enemy choose {}.".format(computer_choice))
        next_of()

    if your_choice == "2" and computer_choice == "Scissor":
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        print("Enemy choose {}.".format(computer_choice))
        next_of()
    elif your_choice == "2" and computer_choice == "Rock":
        print("It's a row. Enemy choose {}.".format(computer_choice))
        next_of()
    elif your_choice == "2" and computer_choice == "Paper":
        print("You loose, enemy choose {}.".format(computer_choice))
        next_of()

    if your_choice == "3" and computer_choice == "Paper":
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        print("Enemy choose {}.".format(computer_choice))
        next_of()
    elif your_choice == "3" and computer_choice == "Scissor":
        print("It's a row. Enemy choose {}.".format(computer_choice))
        next_of()
    elif your_choice == "3" and computer_choice == "Rock":
        print("You loose, enemy choose {}.".format(computer_choice))
        next_of()

    else:
        print(bcolors.WARNING + "Error! Your choice must be between 1-3" + bcolors.ENDC)
        next_of()