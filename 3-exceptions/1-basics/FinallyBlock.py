# !Use nano and the playground dir to show demo code [create a file to use]! !Delete before sharing code!

path = 'GeneralExceptions.py'

# There are times in Python that we need to work with resources like: 
#				files; 
#				DB connections; 
#				network connections; 
#				...

# And if we are using certain resources we should always close those resources at the end of our program.

# We can handle this in the following way:

# BAD WAY:

try:
	file = open(path)
	file.write('Would be to easy right?')
except OSError as oe:
    file.close()
    print('Something went wrong with IO operation')
else:
    file.close()

# GOOD WAY, no code duplication [good programmers avoid that shit].

try:
    file = open(path)
    file.write('Would be to easy right?')
except OSError as oe:
    print('Something went wrong with IO operation')
finally:
    file.close()  # This way even if an exception is raised the resource used will be closed.
