# You know the drill, we need variables to play with:

quote_lucy = """Humans consider themselves unique so they've rooted their whole theory of existence on their uniqueness.
One is their unit of measure, but it's not. All social systems we've put into place are a mere sketch. 
One plus one equals two. That's all we've learned, but one plus one has never equaled two. 
There are, in fact, no numbers and no letters. 
We've codified our existence to bring it down to human size to make it comprehensible. 
We've created a scale so that we can forget its unfathomable scale.
"""

chars = list(quote_lucy)

# We can use a for loop:

for char in chars:
    print(char)

# If we use the enumerate function we get a Tuple returned holding the index en value:

for char in enumerate(chars):
    print(F'index: {char[0]} value: {char[1]}')

# Lets clean up the out print using the unpacking technique:

for index, value in enumerate(chars):  # Tuples can be unpacked
    print(F'index: {index} | value: {value}')
