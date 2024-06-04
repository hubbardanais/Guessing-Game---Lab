"""A number-guessing game."""

from random import randrange

# greet player
print("hello there!")

# get player name
name = input("\nWhat's your name? ")

# choose random number between 1 and 100
random_num = randrange(1, 100)

guess_counter = 0

# repeat forever:
while True:
    guess = input(f"\nAlrighty, {name}! Guess a number! ")
    guess = int(guess)
#     get guess
#     if guess is incorrect:
    if guess != random_num:
        if guess > random_num:
            print(f"\n{guess} is too high! Try again!")
        if guess < random_num:
            print(f"\n{guess} is too low! Try again!")
        guess_counter += 1

    else:
        print(f"\nCongratulations, you won in only {guess_counter} tries!")
        break
#         give hint
#         increase number of guesses
#     else:
#         congratulate player