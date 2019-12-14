#--- Second Attempt ---#

import random

def guess_number(random_number, message, max_guesses, total_guesses = 1):

    if (total_guesses > max_guesses):
        print("Sorry, the correct number was " + random_number + ".")

    guess = input(message)

    if (int(guess) == random_number):
        print("Nice guess! " + guess + " was the correct answer!")

    if (int(guess) < random_number):
        return guess_number(random_number, "Sorry, the number is higher than " + guess + ". Please guess again: ", max_guesses, total_guesses =+ 1)

    if (int(guess) > random_number):
        return guess_number(random_number, "Sorry, the number is lower than " + guess + ". Please guess again: ", max_guesses, total_guesses =+ 1)

random_number = random.randint(1,6)
user_name = input("What is your name?: ")
message = guess_number(random_number, user_name.capitalize() + ", guess a number between 1 and 6!: ", 2)


#--- First Attempt ---#

#import random
#random_number = random.randint(1,6)
#user_name = input("What is your name?: ")


#while True:
#    try:
#        guess_number = int(input("Welcome, {}! Please guess a random number between 1 and 6. ".format(user_name.capitalize())))
#        break
#    except ValueError:
#        print("Oops! That was not an integer. Please try again:")
#
#if guess_number == random_number:
#    print("You got it! The correct number was {}! Thanks for playing!".format(random_number))
#
#elif guess_number > random_number:
#    second_guess = input("The number is lower than {}. Please guess again: ".format(guess_number))
#    if second_guess == random_number:
#        print("Well done! {} was the correct answer!".format(random_number))
#    else:
#        print("WRONG! The correct answer was {}. Thanks for playing!".format(random_number))
#
#elif guess_number < random_number:
#    second_guess = input("The number is higher than {}. Please guess again: ".format(guess_number))
#    if second_guess == random_number:
#        print("Well done! {} was the correct answer!".format(random_number))
#    else:
#        print("WRONG! The correct answer was {}. Thanks for playing!".format(random_number))
#else:
#    print("WRONG! The correct answer was {}. Thanks for playing!".format(random_number))
#
