from collections import namedtuple

# If we're working with data classes we probably want to compare them against each other,
# to see if their values are the same.

# So for this example we will make a point class that has 2 attributes: x, y
# We will make 2 instances of this class and compare them


class Point:

    default_col = 'red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# Making two objects that have the same values for x and y:

first_point = Point(4, 20)
sec_point = Point(4, 20)

# Now we can compare them:

print(f"first_point id: {id(first_point)}, sec_point id: {id(sec_point)}")
print(f"first_point has the same values as sec_point: {first_point == sec_point}\n")


# There is actually a friendlier way of doing the same as all the boilerplate code above:

PointTuple = namedtuple('Point', ['x', 'y'])  # ('NameClass', [attributes])

# Create the desired object to compare:

first_point = PointTuple(x=4, y=20)
sec_point = PointTuple(x=4, y=20)

# And now for the comparing part:

print(f"first_point id: {id(first_point)}, sec_point id: {id(sec_point)}")
print(f"first_point has the same values as sec_point: {first_point == sec_point}\n")

# The downside of this namedtuple technique is that the attributes are immutable:

try:
    first_point.x = 420
except AttributeError as ae:
    print(ae)

# This can be fixed by creating a new instance and storing it in the same variable:

first_point = PointTuple(420, 20)  # You can also lose the keyword arguments, and simply supply arguments

print(f"first_point id: {id(first_point)}, sec_point id: {id(sec_point)}")
print(f"first_point has the same values as sec_point: {first_point == sec_point}")

