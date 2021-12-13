# A Lot of times when we work with user input we need to convert that input 
# to a different type [default is a string].

# Let's take a look on how to do that:

x = input('x is: ')
y = input('y is: ')
plus = '+'
equal = '='

# Will concatenate the two strings:

sum_user = x + y
print(F'{x} {plus} {y} {equal} {sum_user}')

# we must convert them to integers before we can add these numbers:

sum_user = int(x) + int(y)
print(F'{x} {plus} {y} {equal} {sum_user}')

# Python is thus a strongly typed language because it does not do implicit casting

# The different possibilities of typecasting are:

# str()
# int()
# float()
# bool()

# Python also knows truthy and falsy

# Falsy values are:
# ""
# 0
# []
# None -> Object that represents the absence of a value [like null in Java/C#]

# Lets do some examples [maybe do this in ipython to avoid this code mess...]:

value_msg = 'The value returned by calling the function bool'
quotes_not_possible_1 = "(\"\") is:"
quotes_not_possible_2 = "(\"False\") is:"

# FIX THIS! [clean code]
print(F'{value_msg}{"(0) is:"} {bool(0)}')
print(F'{value_msg}{"(1) is:"} {bool(1)}')
print(F'{value_msg}{"(-1) is:"} {bool(-1)}')
print(F'{value_msg}{quotes_not_possible_1} {bool("")}')
print(F'{value_msg}{quotes_not_possible_2} {bool("False")}')
