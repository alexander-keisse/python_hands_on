# If you are dealing with very large lists, it can be better to use an array [10.000 values and bigger] to keep
# memory size of the object smaller, but most of all increased speed when iterating over it.
from array import array
from random import randint
import sys
import timeit

# Makes sense:
iteration_times = 10
size_msg = 'Size of'
size_unit = 'in bytes'

# We make a list containing 10_000_001 values and their values are between 1 and 999:

list_numbers = [randint(1, 1000) for numb in range(10000001)]

# We also declare an array containing the same amount of values and the values are in the same range as our list:
# Find out where i stands for: https://docs.python.org/3/library/array.html

array_numbers = array('i', list_numbers[:])


# We define a function to test execution time over n iterations:

def get_the_execution_time(numbers, iterations):
    start_time = timeit.default_timer()
    for count in range(iterations):
        for number in numbers:
            pass  # placeholder, because we dont want anything to happen while iterating.
    else:
        print("--- %s seconds execution time ---" % (timeit.default_timer() - start_time), type(numbers))


# Function that prints information about the size of an argument past in bytes to the console:

def print_size(obj):
    print(size_msg, type(obj), sys.getsizeof(obj), size_unit)


# Now lets time our execution:

get_the_execution_time(list_numbers, iteration_times)
get_the_execution_time(array_numbers, iteration_times)

print()  # Make some space, for readability

# And lets print the size of our objects, you can use the sys module for that [see print_size function ;)]:

print_size(list_numbers)
print_size(array_numbers)

# We declared our array to hold signed int values, what if we tried to put a float in it:

# array_numbers[0] = 3.14  # Uncomment to see type error [shortcut: ctrl + /]

# This is of course no problem for a list:

list_numbers[0] = 3.14

# Find out more about difference between list and array:

# https://www.youtube.com/watch?v=2vmvtxHVPJI
# https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use
