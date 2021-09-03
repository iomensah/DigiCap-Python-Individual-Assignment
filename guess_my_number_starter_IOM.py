"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

# import random is the entry point of the code to aid generate random integers
import random
# the random number generated is assigned the variable "random_number"
random_number = (random.randint(0, 99))
# Opening statement to the user
print("I am thinking of a number between o and 99")
# user's input is assigned the variable "guess"
guess = int(input("Enter a guess: "))
# the condition to evaluate the user's input if it is incorrect
while random_number != guess:
    if guess < random_number:
        print("Your guess is too low")
        guess = int(input("Enter a new guess: "))
    else:
        print("Your guess is too high")
        guess = int(input("Enter a new guess: "))
# the printout statement if the user's input is correct
print("Congrats! The number was: " + str(random_number))
