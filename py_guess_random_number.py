import random
random_number = random.randint(1,6)
user_name = input("What is your name?: ")


while True:
    try:
        guess_number = int(input("Welcome, {}! Please guess a random number between 1 and 6. ".format(user_name.capitalize())))
        break
    except ValueError:
        print("Oops! That was not an integer. Please try again:")

if guess_number == random_number:
    print("You got it! The correct number was {}! Thanks for playing!".format(random_number))

elif guess_number > random_number:
    second_guess = input("The number is lower than {}. Please guess again: ".format(guess_number))
    if second_guess == random_number:
        print("Well done! {} was the correct answer!".format(random_number))
    else:
        print("WRONG! The correct answer was {}. Thanks for playing!".format(random_number))

elif guess_number < random_number:
    second_guess = input("The number is higher than {}. Please guess again: ".format(guess_number))
    if second_guess == random_number:
        print("Well done! {} was the correct answer!".format(random_number))
    else:
        print("WRONG! The correct answer was {}. Thanks for playing!".format(random_number))
else:
    print("WRONG! The correct answer was {}. Thanks for playing!".format(random_number))

