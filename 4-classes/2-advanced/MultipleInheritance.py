# In Python a class can have multiple base classes,
# similar to multi-level inheritance it can create issues when not used correctly.

# In this example we make a Manager class which has 2 sub classes: Employee, Person:


class Employee:

    def greet(self):
        print('Employee greets')


class Person:

    def greet(self):
        print('Person greets')


# Change the position of base classes defined in the Manager class to see different result in printout.
class Manager(Employee, Person):

    pass


# We make an object to play with:

manager = Manager()

# Python checks the Manager class first if there is no own implementation it goes looking in to the base classes,
# Because the Employee class is the first base class defined it will execute that implementation of the greet method.

manager.greet()

# If inheritance is that bad why should we use it?

# Inheritance is not a bad thing but becomes one if not done well.
# Inheritance can create bugs when classes used for inheritance share behaviours.

# Here you can see an abstract example of good inheritance:


class Flyer:

    def fly(self):
        print('flying, whiiiii')


class Swimmer:

    def swim(self):
        print('big fish small fish, swimming under water')


class FlyingFish(Flyer, Swimmer):

    pass

# When using multiple inheritance we try to avoid common things in our classes!


exocoetidae = FlyingFish()  # Fancy name for flying fish. No you wrong Pycharm [about the typo]!

exocoetidae.swim()
exocoetidae.fly()
