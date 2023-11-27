from random import shuffle
from time import sleep

def player_guess():
    guess = ""

    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number (0-2)!")

    return int(guess)

def check_guess(cups, guess):
    if cups[guess] == "O":
        print("You win!")
    else:
        print("You lose :(")
    
    print(cups)


cups = [" ", "O", " "]
print("Welcome to CUPS!\nGuess in which cup the ball is")
print(cups)
input("Press enter to shuffle")
print("Shuffling...")
sleep(1.0)
shuffle(cups)

guess = player_guess()

check_guess(cups, guess)