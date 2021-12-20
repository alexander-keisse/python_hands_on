# Just like there are instance | class attributes the same can be said about methods.
# We continue on our Point class:


class Point:

    # We can also declare class attributes that are shared across all instances of this class:
    default_col = 'red'

    # Constructor incoming:
    def __init__(self, x, y, z):  # Instance method, we use these if we want to do something to an instant of a Class
        self.x = x
        self.y = y
        self.z = z

    # In some cases you want to make an instance, with some default values [read: point = Point(0, 0)].
    # For such a thing you can define a class level zero method, we call these kind of methods: Factory methods.

    @classmethod  # learn more about decorators: https://www.python.org/dev/peps/pep-0318/
    def zero(cls):
        return cls(0, 0, 0)

    def draw(self):  # Instance method
        print(f'Point ({self.x}, {self.y}, {self.z})')


# Now we can put our factory to work:

point = Point.zero()

# Check the results of our hard working factory:
point.draw()
