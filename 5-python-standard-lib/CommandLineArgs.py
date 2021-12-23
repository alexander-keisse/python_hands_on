import sys

# In this file we're going to take a look at how we can take advantage of arguments given trough an cli

# We will run our code from the command line, this is very easy to do in Pycharm,

# 1. Open the terminal tab in bottom of the screen
# 2. This will open at the root of your project navigate to directory of the CommandLineArgs.py file
# 3. run the python3 CommandLineArgs.py arg1 arg2 12 arg4 2,14 command

# Now let's run it from here, what difference do you see?
print(sys.argv)  # First argument is always present that being the name of our class, with n optional more args given.

# Because we know our list will always return 1 item when no optional arguments are given we can do the following:

if len(sys.argv) == 1:
    print('No optional arguments given.')
else:
    sys.argv.pop(0)
    for n in sys.argv:
        print(f"Optional param: {n}.")
    else:
        print('No more arguments found.')
