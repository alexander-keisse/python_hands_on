# Makes sense:

new_line = '\n'

# Lets make a list to play with:

numbers = list(range(5))


# Sometimes you want individual items out of your list and assign them to variables
# This is how you would do it in most languages, also works in Python:

first = numbers[0]
second = numbers[1]
last = numbers[-1]

# Lets see what we found:
print(F'[0]: {first}')
print(F'[1]: {second}')
print(F'[4]: {last}', new_line)  # lets create some space between examples ;)


# Now lets take a look at unpacking lists, use the Python powah!
# On the left side we need to declare as many variables as there are values in the list!:

first, second, third, fourth, fifth = numbers

# Lets see what we get:
print(F'[0]: {first}')
print(F'[1]: {second}')
print(F'[2]: {third}')
print(F'[3]: {fourth}')
print(F'[4]: {fifth}', new_line)


# We need a new list to play with, make it a bigger one:

huge_list = list(range(1001))


# This unpacking in Python is very powerful, but what if we have a huge list and are only
# interested in the three first values of that list:

first, second, third = huge_list[:3]  # Works, but maybe not ideal in every situation

# Lets see what we get:

print(F'[0]: {first}')
print(F'[1]: {second}')
print(F'[2]: {third}', new_line)


# You can do this slightly different too, lets say you also need the other
# values so you want to store those in a separate list called others:

first, second, *others = huge_list[::-1]  # Reversed the list to keep it interesting

# Show what we have stored in our variables:

print(F'[0]: {first}')
print(F'[1]: {second}')
print(F'List with remaining values: {others}', new_line)

# What if we want the first and last number of the list:

first, *others, last = huge_list[::-1]

# Lets print out the results:
print(F'[0]: {first}')
print(F'[1001]: {last}')
print(F'List with remaining values: {others}')
