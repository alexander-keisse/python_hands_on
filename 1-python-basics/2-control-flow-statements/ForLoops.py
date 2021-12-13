# Think about it makes sense ;)
new_line = '\n'

# In python with for loop we can iterate over every object that is iterable (Makes sense right?)
for x in 'Python':
    print(x)  # In each iteration our x variable will hold one character

# To separate examples
print()

# We can iterate over list:

for val in ['a', 'b', 'c']:
    print(val)

# To separate examples
print()

# If we want to iterate over a range of numbers:

for num in range(10):
    print(num)

# To separate examples
print()

# We can even go further and give 1-start and end values [end is exclusive, 1-start inclusive]:

for num in range(5, 10):
    print(num)

# To separate examples
print()

# Lets go beyond sanity, and define the steps taken:

for num in range(0, 10, 2):
    print(num)

# Unlike what you probably think the function range does not give back a list, look:

print(new_line, range(5))
print(new_line, [0, 1, 2, 3, 4])  # For comparison this is a printout of a list.

# But if not a list what is this kind of magic:

print(new_line, type(range(5)))  # Ah yes, an object of the class 'range' you say.

# TL;DR
# 'range' objects in python are iterable, just as strings and lists, that's why we can use
# them in for loops. Now what is interesting of these range objects is that they take a small
# amount of space or memory

# instead of having a list with 5 million numbers you have a small object that can be iterated over
# in each iteration it will produce a new number starting from 0:

range(5_000_000)


# If you want to make it a list:

list_numbers = list(range(10))
print(new_line, list_numbers)
print()

# Yes, follow the white rabbit: https://docs.python.org/3/library/stdtypes.html#range

# Using the break statement:

for i in range(10):
    if i == 5:
        break
    print(i)

print()

for i in range(10):
    if i == 5:
        continue
    print(i)


# How to find prime numbers in python using double for loop

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f'{n} equals {x} * {n//x}')
            break
    else:
        print(f'{n} is a prime number')
