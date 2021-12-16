# Makes sense:

new_line = '\n'

# List to play with, remember a lazy programmer is a good programmer:

letters = list('alexander')  # dont do it like ['a', 'l', 'e', 'x', 'a', 'n', 'd', 'e', 'r'], use brain!

# Add to the end of the list:

letters.append(' ')

# We can also use a string with for loop to add the different chars of a string:

for char in 'keisse':
    letters.append(char)  # When a function belongs to an object we speak of a method ;)

# Print out the list of letters:
print(letters, new_line)

# If you want to add some value at a certain index we can use the insert() method:

for index, char in enumerate('name of student: '):  # Here I use unpacking -> Tuple
    letters.insert(index, char)  # I can use the index, to insert in the beginning of the list

# Lets print the result:
print(letters, new_line)

# Remove from the list:

removed_last_index = letters.pop()

# Again lets check the result:
print(F'Removed value, from last index: {removed_last_index}', new_line)
print(F'Lets have a look if our list changed: {letters}', new_line)  # It did change, last index was removed

# What if you wanted to remove the first index, you can do this as follows:

letters.pop(0)
print(F'Changed list: {letters}', new_line)

# What if I want to remove the first value e that we come across in our list of letters,
# but dont know the index, look below for the answer:

letters.remove('e')
print(F'Watch the third index, you can compare with printout above: {letters}', new_line)

# WARNING: Return after FilterFunction.py

# Lets remove all them e value bastards:

# First step:
# Replace all e chars with falsy values

letters = [s.replace('e', '') for s in letters]
print(F'the char e got replaced, fear me char e: {letters}, ', new_line)

# Second step:
# Filter function checks for Falsy values and throws them out, result is a new list after we cast it.

letters = list(filter(None, letters))
print(F'I have my sanity back: {letters}', new_line)

# Last way to remove from a list:
del letters[0:6]
print(F'What is left: {letters}', new_line)

# Drop mic:
letters.clear()
print(F'Kneel before me list: {letters}')
