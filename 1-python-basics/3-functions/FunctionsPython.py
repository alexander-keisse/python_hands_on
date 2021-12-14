from random import randint


# We define our first function, in its most basic form [function definition, hence its name def]:

def function_name(parameter_list):
    pass  # 2 empty lines between function is Python convention


# So lets give this some meaning:

def increment_pass(number, by):
    pass  # This is a placeholder, if the programmer is not concerned yet about implementations


print(increment_pass(2, 5))  # This will print a None object, because of default behaviour function.


# So lets give this function some meaning:

def increment(number, by):
    return number + by  # The augmented operator [number += by] is not allowed in a return statement


print(increment(2, 3))


def increment_by_one(number, by=1):
    return number + by


print(increment_by_one(2))  # This way we can set a default value to our parameter [1]
print(increment_by_one(2, 5))  # If we give the second parameter default value is dropped


# We can even give back multiple values:

def return_multiple_values():
    # We can use randint to generate random value integer
    return randint(0, 100), randint(0, 100), randint(100, 1000)


print(return_multiple_values())  # What we get back is called a tuple [basically read only list]


# You want more control see below:

def add(first_val: int, second_val: int) -> int:
    return first_val + second_val

# Now a fellow programmer gets his arguments highlighted so he knows he is using your function
# in another way then its meant [still possible though ;)]:


print(add('a', 'b'))
