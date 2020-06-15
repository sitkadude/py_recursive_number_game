#--- Rewritten Recursively ---#
import random

def guess_number(random_number, message, max_guesses, total_guesses = 1):

    if (total_guesses > max_guesses):
        return print(f"Sorry, {user_name}. The correct number was {str(random_number)}!")

    while True:
        guess = input(message)
        try:
            if (int(guess) == random_number):
                return print(f"Nice guess, {user_name}! {guess} was the correct answer!")
            else:
                break
        except ValueError:
            print(f"Sorry, {user_name}. That was not an integer, please try again!")
            continue

    if (int(guess) < random_number):
        return guess_number(random_number, f"Sorry, {user_name}. The number is higher than {guess}. Please guess again: ", max_guesses, total_guesses + 1)

    if (int(guess) > random_number):
        return guess_number(random_number, "Sorry, {user_name}. The number is lower than {guess}. Please guess again: ", max_guesses, total_guesses + 1)

random_number = int(random.randint(1,6))
user_name = input("What is your name?: ").title()
message = guess_number(random_number, f"{user_name}, guess a number between 1 and 6!: ", 2)


#--- Non-Recursively ---#

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
