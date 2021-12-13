result_msg = "result is:"

print("Let's start with the Arithmetic operators")

first_numb = int(input('Fill in a number:\n'))
second_numb = int(input('Fill in another number:\n'))

print("\nRESULTS:\n")

# addition:

result = first_numb + second_numb
print(F'{first_numb} {"+"} {second_numb} {result_msg} {result}')

# subtraction:

result = first_numb - second_numb
print(F'{first_numb} {"-"} {second_numb} {result_msg} {result}')

# multiplication:

result = first_numb * second_numb
print(F'{first_numb} {"*"} {second_numb} {result_msg} {result}')

# division:

result = first_numb / second_numb
print(F'{first_numb} {"/"} {second_numb} {result_msg} {result}')

# Loose floating point value:

result = first_numb // second_numb
print(F'{first_numb} {"/"} {second_numb} {result_msg} {result} {" [without floating value]"}')

# Rest modulus:

result = first_numb % second_numb
print(F'{first_numb} {"%"} {second_numb} {"remainder is:"} {result}')

# With the powah of python:

result = first_numb ** second_numb
print(F'{first_numb} {"^"} {second_numb} {result_msg} {result}')


# Using a augmented operator possibilities:
# If you want to try this out, uncomment one by one

# addition
# total = first_numb += second_numb

# subtraction
# total = first_numb -= second_numb

# multiplication
# total = first_numb *= second_numb

# division
# total = first_numb /= second_numb

# Loose floating point value
# total = first_numb //= second_numb

# Rest modulus:
# total = first_numb %= second_numb

# With the powah of Python
# total = first_numb **= second_numb

# Printout result
# print(total)  # You cant use augmented operators in the built in print function!
