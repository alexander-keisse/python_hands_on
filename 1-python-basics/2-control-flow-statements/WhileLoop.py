import random

# Variables oh how I love to play with them:

guess = 0
answer = random.randint(0, 100)

# Mini game that uses user input to check vs a randomly created
# answer, when guessed correctly game is ended:

while answer != guess:
    guess = int(input('Make a guess [0-100]'))  # We know will get a string back so we cast it to integer
    if answer < guess:
        print('Lower!')
    elif answer > guess:
        print('Higher!')

else:  # Only triggered if the while loop is ended without a break statement
    print('You guessed right!')
