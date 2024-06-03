"""A number-guessing game."""

from random import randrange

# greet player
print("hello there!")

# get player name
name = input("\nWhat's your name? ")

# choose random number between 1 and 100
random_num = randrange(1, 100)

# repeat forever:
#     get guess
#     if guess is incorrect:
#         give hint
#         increase number of guesses
#     else:
#         congratulate player