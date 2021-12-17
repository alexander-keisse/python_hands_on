from timeit import timeit

# In the RasingExceptions.py we learned how to raise an exception but this comes at a cost.
# !!This does not work in ipython, ipython has it's own timeit function!!

# To learn more about this we will time our execution time after x times iteration:

# The first thing we have to do is convert our code to be examined in to a string as such:

code_1 = """
def calculate_x_factor(age):
    if age <= 0:
        raise ValueError('Age cannot be 0 or less.')
    return 42 / age


try:
    calculate_x_factor(-27)
except ValueError as ve:
    pass  # To speed up our code ;)

"""

code_2 = """
def calculate_x_factor(age):
    if age <= 0:
        return None
    return 42 / age


x_factor = calculate_x_factor(-27)
if x_factor == None:
    pass
"""


# This way you can test at which point, raising an exception in you code becomes to high:

print('Execution time of our code with raising exception: ', timeit(code_1, number=10_000))
print('Execution time of our code without raising exception: ', timeit(code_2, number=10_000))

# IMPORTANT:
# If you are building an application where scalability and performance are important,
# it is best to raise an exception where you really need too.
