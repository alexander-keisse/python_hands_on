# Classes are very important in programming languages and this is no different for Python.

# Class: blueprint for creating new objects
# Object: instance of a class

# Class: Human
# Objects: Neo, Elliot, Mr Alexanderson,

# We are going to use the Pascal system for naming our class more info:

# https://en.wikipedia.org/wiki/Naming_convention_(programming)#Python_and_Ruby


class Point:

    def draw(self):
        print('draw')


# We can now make an Object out of our Point Class:

first_point = Point()

# We can use our method defined in the Point Class, but also those inherited from the object

first_point.draw()

# Lets take a look at the type of our point object:
print(type(first_point))  # The __main__ seen in our printout is the name of our module, more about that later.

# Sometimes we have an object and we wanna know if it is an instance of a given class
print('the point object is an instance of the int class: ', isinstance(first_point, int))
print('the point object is an instance of the Point class: ', isinstance(first_point, Point))
