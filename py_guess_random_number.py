import random
random_number = random.randint(1,6)
user_name = input("What is your name? ")
guess_number = int(input("Welcome, {}! Please guess a random number between 1 and 6. ".format(user_name.capitalize())))


if guess_number == random_number:
    print("You got it! The correct number was {}! Thanks for playing!".format(random_number))

elif guess_number > random_number:
    second_guess = input("The number is higher is lower than {}. Please guess again: ".format(guess_number))

elif guess_number < random_number:
    second_guess = input("The number is smaller is lower than {}. Please guess again: ".format(guess_number))
else:
    print("WRONG! The correct answer was {}. Thanks for playing!".format(random_number))

