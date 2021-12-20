# We will be looking in to constructors.

# A constructor is a special method that we can use to create an object of our Point Class.
# Trough this method we can also initialize different attributes [x, y, z, ...].

# TL;DR

# All methods that we define in our class should have at least one parameter: self
# self is a reference to the current Point object, when we create an instance of this class.

# Once we create an object of this class, Python will internally create that object in memory
# and stores that memory address in the attribute self as well.

# Attributes: variables that include data about our objects [human attributes: eye colour, height, weight, ...]


class Point:

    # Constructor incoming:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def draw(self):
        print(f'Point ({self.x}, {self.y}, {self.z})')


# Create an object/instance:
point = Point(420, 18, 27)

# Simply print our attributes:
print('x coordinate:', point.x)
print('y coordinate:', point.y)
print('z coordinate:', point.z)

point.draw()  # The self argument is not needed, because Python fills this in for us.
