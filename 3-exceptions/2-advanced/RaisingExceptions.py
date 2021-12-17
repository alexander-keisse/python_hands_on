# I have covered how to handle exceptions in the GeneralExceptions.py class.
# But we can also raise exceptions our self, let me show you an example on how to do this:


def calculate_x_factor(age):
    if age <= 0:
        raise ValueError('Age cannot be 0 or less.')
    return 42 / age


# I are good programmer:

try:
    calculate_x_factor(-27)
except ValueError as ve:
    print(ve)
