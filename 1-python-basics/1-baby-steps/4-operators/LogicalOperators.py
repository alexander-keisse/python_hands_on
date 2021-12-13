# Lets make a variable to play with:

name = 'Alex'
empty_name = ''
spaces_string = ' '

# In Python we have 3 logical operators:

# and
# or
# not

# Lets take a look at some examples with not operator:

if name and spaces_string:  # We are using the fact that an empty string is Falsy
    print("String variables contain a string value")

if not empty_name:
    print("empty_name is empty")

# To check if the value of our variable is not simply whitespaces:

if not spaces_string.strip():
    print("spaces_string is actually an empty string after removing the spaces")

# Create a new variable to play with:

age = 12

# Now lets use the and operator:

if age >= 18 and age < 65:
    print("Eligible")

# And for completeness the or operator:

if False or 1:
    print('1 is True')

# This is called chaining comparison operators

age = 21

if 18 <= age < 65:
    print('chaining comparison operators: 18 <= age < 65')
