# Lets 1-start by making a variable to play with:

age = 20
print(type(age))  # check its data type

# Lets change our value:

age = 'Python'
print(type(age))  # again check it's type

# Printout to see what the value is:

print(age)

# If we want to prevent this:

int_value: int = 2  # We can hint want we expect our type to be
print(type(int_value))

# We will need to use a lint to check this type ref and throw compile error:

int_value = 'hello'
print(type(int_value))

# Still works because we don't have a lint checking!!:

print(int_value)

# Check this out to learn more about lints: https://www.pylint.org/
