#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Nov 2021
# this program does the number guessing game

import random


def main():
    # this program checks to see if the number guessed is the random number

    # input
    guess = input("Enter a number between 0-9: ")
    random_number = random.randint(0, 9)  # a number between 0 and 9

    # process & output
    try:
        guess = int(guess)
        if guess == random_number:
            print("You guessed correct")
        else:
            print("Incorrect , The number was " + format(random_number))
    except Exception:
        print("{} is not an integer".format(guess))

    print("Thanks for playing .")
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
