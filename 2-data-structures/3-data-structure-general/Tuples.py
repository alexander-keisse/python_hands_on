# In this class we will take a closer look at Tuples:

# It is basically a read only list, we can use it to contain a sequence of objects,
# but we cant modify this sequence, okay enough talk lets start:

points = (1, 2)  # Values inside represent X and Y values

# This notation is also valid:

sec_points = 1, 2

# We can also use this notation with 1 value:

third_points = 1,  # Remove the ',' for different result printout; Tuple with 1 item needs trailing comma
makes_no_sense = ()  # Empty tuple [parentheses NOT optional]

# We can verify that we made Tuples using the built in function type:

print(type(points))
print(type(sec_points))
print(type(third_points))
print(type(makes_no_sense))

# We can also concatenate different Tuples together:

combined = (42, 29) + (27, 420)
print(combined)

# If you want to enlarge the Tuple with duplicate values:

combined *= 3
print(combined)

# To convert a list to a Tuple use the built-in function tuple():

list_points = list(range(1, 101))
tuple_points = tuple(list_points)

# Let's check the result:
print(tuple_points)

# We can do this with a string too:

char_tuple = tuple('Alexander')

# Let's check the result:
print(char_tuple)

# Access an individual index just like a list:

print(char_tuple[:4])  # Or a slice of the Tuple: char_tuple[0:4]

# Has allot of the same features as list, but you simply cant modify the values of a Tuple.
# So no adding, removing functions as is the case with list.

# Find out more: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
