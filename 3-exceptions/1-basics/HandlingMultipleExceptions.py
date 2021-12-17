# Try and see what happens if you put 0 as the input in our console

try:
    age = int(input('Please fill in your age: '))
    x_factor = 42 / age
except ValueError:
    print('You did not enter a valid age!')
else:
    print('Put in a valid number, so that you can continue execution beyond this point ;)')

# In math just as in Python we can't divide by zero of course, so we need to handle multiple exceptions:

try:
    age = int(input('Please fill in your age: '))
    x_factor = 42 / age
except ValueError:
    print('You did not enter a valid age!')
except ZeroDivisionError:
    print('You can not divide a number by zero!')
else:
    print('Executed if and only if there was no exception thrown!')

# What if all our different except blocks would do the same, how could we handle this?
# Well let me show you!

try:
    age = int(input('Please fill in your age: '))
    x_factor = 42 / age
except (ValueError, ZeroDivisionError):
    print('We are all the same')
except ZeroDivisionError:
    print('If you put in 0 as input, '
          'Python will never reach these lines because it is already handled in the except block above!')
except KeyboardInterrupt:
    print('This is used a lot for halting programs in Python')
