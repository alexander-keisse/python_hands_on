# Here are some different way's to work with string literals:

# Try this out in an ipython session...

# 'This is a literal string'
# "This is another string"
#
# 'I\'m a Python fanatic'  # a quote can be escaped
# "I'm a Python fanatic"  # this way is more readable
#
# 'A not very long string\
# that spans on two lines'  # comment not allowed on previous line
#
# 'A not very long string\n\
# that prints on two lines'  # comment not allowed on previous line
#
# """An even bigger
# string that spans
# three lines"""  # comment not allowed on previous lines
#
# the_text = """\
# First line
# Second line
# """  # like 'First line\nSecond line\n' but more readable

# Let's make a variable to work with:

course_name = 'Python course'

# if we want to know how many chars a String contains:

print(len(course_name))

# if we want a certain char in a String we can do:

print(course_name[0])

# In python we can also use a negative index:

print(course_name[-1])

# We can also slice a String:

print(course_name[0:6])  # Second arg is exclusive

# this notation does the same

print(course_name[:6])

# And of course this is also possible

print(course_name[7:])

# The python interpreter will always reserve a new memory location for the char/s taken:

print(id(course_name))
print(id(course_name[:]))  # Why is this the same address ;) [mutable]
print(id(course_name[5:]))  # "New Value" so it needs his own memory address

# You can also make a string object like so:

marypop = ('supercalifragilistic'  # Open paren->logical line continues
           'expialidocious')      # Indentation ignored in continuation.

# The string assigned to marypop is a single word of 34 characters:

print(marypop)
