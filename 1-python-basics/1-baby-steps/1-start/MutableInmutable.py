# Reserving memory space:

x = 420

# Lets lookup the memory location:

print(f'memory address of variable x: {id(x)}, value: {x}')

# String, boolean and Integers are immutable so the python interpreter
# will allocate a new memory location if we alter the value of a variable:

x = 42
print(f'memory address of variable x: {id(x)}, value: {x}', '\n')

# Lists however are mutable objects:

list_numbers = [1, 2, 3]
print(f'memory address of variable list_numbers: {id(list_numbers)}, value: {list_numbers}')

# Lets see what our memory address is after some changes:

list_numbers.append(4)
print(f'memory address of variable list_numbers: {id(list_numbers)}, value: {list_numbers}')

# BONUS PART

# Learn more:
# Memory management in Python: https://www.youtube.com/watch?v=F6u5rhUQ6dU
