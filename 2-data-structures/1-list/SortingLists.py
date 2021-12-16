from random import randint

# Makes sense:

new_line = '\n'

# Lets create a list of 10 values with random numbers:

numbers = [int(randint(0, 100)) for number in range(10)]

# Lets print our list
print(F'{"Unsorted beginning state:"} {numbers}', new_line)

# We do a sort and check again:

numbers.sort()
print(F'{"List is now sorted in ascending order:"} {numbers}', new_line)

# If we want to sort in descending order we can use a keyword argument:

numbers.sort(reverse=True)
print(F'{"List is now sorted in descending order:"} {numbers}', new_line)

# In addition to the sort() method, we have the built-in function sorted():

returned_new_list = sorted(numbers)

# Always a good id to check the id [memory reference]:

print(id(returned_new_list))
print(id(numbers), new_line)

# It's not because you declare a new variable, that it automatically
# gets a new memory location, just to make a point, uncomment to see:

# new_list = returned_new_list
# print(id(new_list))
# print(id(returned_new_list))

# Lets have a print out to see that its sorted in ascending order:
print(F'Ascending order: {returned_new_list}')


# Lets reverse that in to descending order:
print(F'Descending order: {sorted(returned_new_list, reverse=True)}')
