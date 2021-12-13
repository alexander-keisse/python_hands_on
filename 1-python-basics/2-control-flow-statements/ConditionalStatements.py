# IMPORTANT:
# TABS AND SPACES DONT MIX IN PYTHON

# Variable to play with
age = 22

# Pythonic way to use if statement:

if age:
    print('Will only execute if the age variable is evaluated as True [which it will...], '
          'meaning it holds a value and not None.')

# Do not use any of the following:

# if age is True: pass
# if age == True: pass
# if bool(age): pass  # When using a simple statement, you can do it on the same line as the header line of the clause

# Let's take a look at a conditional statement with multiple statements:

if age >= 18:  # Because we don't have {} in Python we dont need to argue where to put them for 2 decades.
    print("You're an:")
    print('Adult')  # indented code belongs to if statement

elif age >= 13:  # To start an elif construction, it needs to be indented the same as the if statement
    print("You're a teenager")

else:  # And of course we can use the else statement.
    print('Child')

# This part is after our conditional statements...
print("After conditional statement")

# If you want to use empty conditional statements [as a placeholder till implementation] 
# you can use the pass keyword:

if age > 101:
    pass  # Won't compile otherwise
else:
    pass
