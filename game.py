"""A number-guessing game."""

from random import randrange


print("hello there!")

name = input("\nWhat's your name? ")

random_num = randrange(1, 100)

guess_counter = 0

while True:
    guess = input(f"\nAlrighty, {name}! Guess a number! ")
    try:
        guess = int(guess)
    except ValueError:
        print("\nYou have committed a crime. Guess a *number* between 1 and 100!")
        continue
    
    if guess != random_num:
        if guess > 100 or guess < 1:
            print("\nYou have committed a crime. Guess a number between 1 and 100!")
        elif guess > random_num:
            print(f"\n{guess} is too high! Try again!")
        elif guess < random_num:
            print(f"\n{guess} is too low! Try again!")
        guess_counter += 1
        
    else:
        print(f"\nCongratulations, you won in only {guess_counter} tries!")
        break
        
