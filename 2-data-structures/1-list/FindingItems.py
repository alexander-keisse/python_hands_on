# Lets make a list shall we:

letters = list('f society, democracy you say[will be fun they said]')

# If we want to find the index of a certain value:

print(letters.index('e'))

# What if we search the index of a char value that is not included in the list
# print(F'{"Good job on breaking the code:"} {letters.index("a")}')  # Most C like languages return -1

# Do a check first dummy:

if '²' in letters:  # change '²' to an occurring char for different outcome
    print(F'You must be Senior programmer, yes? {letters.index("a")}')  # Comment line 8, dummy

# We can also count the occurrence of a certain value:

char = 'l'  # Change it to '²' and see what happens, no worries ;)
print(F'The char {char} has occurred: {letters.count(char)} times')
