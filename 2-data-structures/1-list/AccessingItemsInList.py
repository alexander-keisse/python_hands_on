# Lets make a list to play with:

letters = ['a', 'b', 'c', 'd']

# If you want to access the first item:

print(f'first item: {letters[0]}')

# The last item can be found as such:

print(f'last item: {letters[-1]}')

# Easy enough right? Ok now lets modify the first item:

# letters[0] = 'A'
letters[0].upper()  # Does the same as the above expression

# Now let's see what happened to our list:

print(letters)

# Just as we can slice strings we can slice our lists:

print(letters[0:3])  # returns the first three elements

# print(letters[:3])  # remember we can leave the first or second argument [Python assumes you start at 0]
print(letters[1:])  # or leave the last index ;)

# If we want a copy of our list:

print(f'original list id: {id(letters)}')
print(f'copied list id: {id(letters[:])}')

# And we can also use steps to determine what will be taken out of our list:

print(letters[::2])

# Lets make a second list to make it a bit more clear:

numbers = list(range(101))
print(numbers[::2])  # this way we get al the even numbers

# We can also reverse the list as follows:

print(numbers[::-1])
