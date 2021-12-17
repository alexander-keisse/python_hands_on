from sys import getsizeof

# In Python we can use generator objects if we are working with big data sets or perhaps an infinite input of data.
# We actually don't want to store al this data in memory, lets take a look at an example:

values = [x * 2 for x in range(1_000_000)]

# Lets take a look at the byte size of this list using the sys module:
print('List size in bytes: ', getsizeof(values))

# Below we can see the syntax for creating a generator object:

generator = (x * 2 for x in range(1_000_000))  # Just like lists, generator objects are iterable

# Lets take a look at the size of our generator obj:
print('Generator object size in bytes: ', getsizeof(generator))
# INFO: Instead of storing all our values in memory, the value gets changed every iteration.

# This generator objects is iterable so we can do the following:
for el in generator:
    pass

# What happens if we enlarge our generator object:

generator = (x * 2 for x in range(1_000_000_000))  # FUN FACT: A list this large would not work [out of memory]

# Watch the Python world burn, if you don't believe:

# print("It's on:")
# values_list = [x * 2 for x in range(1_000_000_000)]
# print('list size: ', getsizeof(values_list))  # interrupted by signal 9: SIGKILL

# What it means: https://stackoverflow.com/questions/19189522/what-does-killed-mean/19192507

# We again print our size expressed in bytes, can you guess what happens:
print('Bigger generator object size: ', getsizeof(generator))  # What a shock! Not really of course :)

# This has some downsides as well, when we use a generator object we can't see how many object we will be working with:

try:
    print(len(generator))

except TypeError as te:  # We declare the variable te so that we can do something like print the exception in code below
    print(f'what happened -> {te}')
