# In Python we have a very powerful data structure to hold key-value pairs: dictionaries.
# We can only use immutable objects as the key [so mostly string is used], the value can be whatever no limitations.

# Makes sense:

new_line = '\n'

first_key = 'x'
second_key = 'y'
third_key = 'z'
invalid_key = 'invalid key'

msg_x = 'The value of x is:'
mem_loc_msg = 'memory location:'

# Let's start by making one to play around with, although we choose the same type for the keys
# remember that mixed key types are possible:

first_point = {first_key: 1, second_key: 2}  # We're using a string as a key and an integer as the value.


# Just as there are functions to create lists, tuples and sets there is a builtin function to make dictionaries:

sec_point = dict(x=1, y=2)  # keyword argument are a bit cleaner then the double/single quotes.


# We can print some information about these objects:

print(F"{first_point} {mem_loc_msg} {id(first_point)}")
print(F"{sec_point} {mem_loc_msg} {id(sec_point)}", new_line)


# we can search values according to keys stating them as index with the brackets notation:

print(F"{msg_x} {first_point['x']}")


# We can't use numeric indexes like we do with lists, so the following syntax will trow an exception:

# print(F"Value of first element: {first_point[0]}")  # comment to continue beyond this line.


# Of course we can change the value as follows:

first_point[first_key] = 5


# Lets see if we modified the value:

print(F"{msg_x} {first_point[first_key]}", new_line)


# We can add key-value pairs in the same way:

first_point[third_key] = 14


# Lets see if that worked:

print(F"{first_point} {mem_loc_msg} {id(first_point)}", new_line)


# If you would search for a value using an invalid key we get a KeyError, but good programmers check before:

if invalid_key in first_point:
    print('Never gonna get here, so no error for you! Good job', first_point[invalid_key])


# Better even would be to use the get() method, this will return None if the key is invalid [uncomment to see diff]:

print(F"Value returned when using a invalid key: {first_point.get(invalid_key)}", new_line)
print(first_point.get(invalid_key, first_point[first_key]))  # We return a None object if the key is not found.


# We can also use the del statement to take a key-value pair out of our dictionary:
del first_point[first_key]


# Lets take another look:

print(F"{first_point} {mem_loc_msg} {id(first_point)}", new_line)


# We can loop over our keys, and use the key to retrieve the corresponding value:

for key in first_point:
    print(F"Key: {key} Value: {first_point.get(key)}", new_line)


# We can also iterate over our dictionary returning a tuple holding the key and value:

for t in first_point.items():
    print(t)
else:
    print()  # This closing action could be used for something useful, like cleaning up resources, trigger an event, ...

# We can of course unpack the tuple:

for key, value in first_point.items():
    print(F"The key: {key} holds the value: {value}")
