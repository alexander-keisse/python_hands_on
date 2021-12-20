# Makes sense:

new_line = '\n'

# The magic method __add__ can be overwritten, when done you can add 2 instances using the add operator.
# You can see 2 different cases that can be useful.

# Example 1:


class Human:

    def __init__(self, surname, name, intelligence):
        self.surname = surname
        self.name = name
        self.intelligence = intelligence

    def __str__(self):
        return f'{self.surname} {self.name}'

    # In this implementation the attributes get added up, original value of the instance attributes wont be changed.
    def __add__(self, other):
        return self.intelligence + other.intelligence


elliot = Human('Sam', 'Esmail', 9001)
snoop = Human('Snoop', 'Lion', 420)

print(f'Combined intelligence: {snoop + elliot}{new_line}')

# Example 2:


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # In this implementation we will create a new instance and return that instance,
    # in this way we can create a combined instance.
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


# Create 2 instances of the Point class to play with:

first_point = Point(14, 45)
sec_point = Point(84, 3)

combined = first_point + sec_point  # Store the newly created instance in a new variable

# Lets check our result:
print(f'value of x: {combined.x}, value of y: {combined.y}{new_line}')
print(combined)  # Shouldn't be a surprise, because we did not overwrite the magic method __str__
