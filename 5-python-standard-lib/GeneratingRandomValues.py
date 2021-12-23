import random
import string

# Makes sense:

new_line = '\n'

# In this class we are going to take a look at how we can generate random values in Python.

# In order to generate a random floating point number between 0 and 1:

print(f"Random number between 0 and 1: {random.random()}{new_line}")

# We can also use the random module for generating int values:

print(f"Random integer value between 1 and 10: {random.randint(1, 10)}{new_line}")

# We also have a way to pick a random value out of a given list:

print(f"Random value out of a list [choice method]: {random.choice(range(1, 5))}{new_line}")  # Remember 5 is exclusive!

# Or we can take out multiple values out of our list, using the keyword argument k= we can define how much values:

print(f"Random values out of a list [choices method]: {random.choices(range(1, 11), k=5)}{new_line}")

# How about we make a random password:

# The values we need to make such a password could be in a hard coded string or we are smart and use the following:

print(string.ascii_letters)
print(string.digits, new_line)

# Okay so now we know where to take our values from, lets do this:

print(f"Random password first attempt: {random.choices(string.ascii_letters + string.digits, k=8)}{new_line}")

# Like you saw in the first attempt we have our random values to make our password but how about we put them together:

print(f"Random password second attempt: {''.join(random.choices((string.ascii_letters + string.digits), k=22))}")

# Making a list to play around with:

numbers = list(range(1, 11))
print('printout of numbers before random shuffle: ', numbers)

# Lets shuffle the values of our list:

random.shuffle(numbers)

# printout what we get:
print(f"printout of numbers after random shuffle: {numbers}")
