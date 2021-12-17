# !Use nano and the playground dir to show demo code [create a file to use]! !Delete before sharing code!

# Makes sense:

path = 'CostlyExceptions.py'
sec_path = 'RaisingExceptions.py'

# There is a way in Python that closes certain (not all!) resources automatically,
# this means our finally block is not needed anymore.

try:
    with open(path) as file:  # This way the close function is called whatever happens.
        print('File is opened.')
except OSError:
    print('IO exception occurred, fix that shit bro!')

# We can also do this with multiple resources as well:

try:
    with open(path) as file, open(sec_path) as sec_file:
        print('File is opened.')
        # if an object has these 2 methods[L22/L23] it means that it can be used in the with statement.
        # These objects support contact management protocol, more about this in the class package.

        # file.__enter__()  # We call these kind of methods, magic methods.
        # file.__exit__()
except OSError:
    print('IO exception occurred, fix that shit bro!')
