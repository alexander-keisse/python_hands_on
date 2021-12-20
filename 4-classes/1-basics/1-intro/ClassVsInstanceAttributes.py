# Because Python is a dynamic language [as is JS for example],
# We can define our attributes in other ways then just in the constructor.


class Point:

    # We can also declare class attributes that are shared across all instances of this class:
    default_col = 'red'

    # Constructor incoming:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def draw(self):
        print(f'Point ({self.x}, {self.y}, {self.z})')


first_point = Point(54, 44, 78)

# Because of the dynamic character of the language we can do the following:

first_point.foo = 'bar'
print('foo: ', first_point.foo, '\n')

# x; y; z; foo are all instance attributes,
# this means if we make a second instance of this object we can store different values in these attributes:

sec_point = Point(24, 55, 74)

# Dont believe well check this out:

first_point.draw()
sec_point.draw()
print()

# If we want to print our Class attribute default_col we can do this in the following ways:

print('instant ref default color: ', first_point.default_col)  # Instance reference
print('class ref default color: ', Point.default_col, '\n')  # Class reference

# Now lets burn the world down:

Point.default_col = 'green'
first_point.default_col = 'yellow'

print('first instant ref default color: ', first_point.default_col)  # Instance reference
print('second instant ref default color: ', sec_point.default_col)  # Instance reference

print('class ref default color: ', Point.default_col)  # Class reference

# In practical sense you will most likely use instance attributes;
# but there are of course places where you want class attributes over instance attributes!
