# Look at ListComprehension if you have forgotten the comprehension theory.
# Lets do an example of dictionary comprehension:

random_chars = {x: chr(x * 50) for x in range(11)}  # Using the built-in function chr() to convert integers to chars.

# Lets see what we got here using the unpacking technique:

for key, value in random_chars.items():
    print(F"{'The key'} {key} {'holds the value'} {value}")


# We can use comprehensions with: List, Sets and dictionaries but what about tuples:

rand_tuples = (x for x in range(11))

# Let's see what we get here:

print(rand_tuples)  # Spoiler alert: the above code returns a generator obj more about that in GeneratorObjects.py
