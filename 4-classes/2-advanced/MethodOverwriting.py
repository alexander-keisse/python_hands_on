# In this class we're going to take a look at method overwriting, this can be useful in a lot of ways.
# We have a constructor in the Animal class, this constructor will be inherited by every subclass,
# Unless we overwrite it.

class Animal:

    def __init__(self):
        print('Animal constructor executed')
        self.age = 10

    def eat(self):
        print('Eating...')

    def __str__(self):
        return f"Animal is {self.age} years old"


class Mammal(Animal):

    # Will overwrite the animal constructor!
    def __init__(self):
        # super().__init__()
        print('Mammal constructor executed')
        self.weight = 2

    def walk(self):
        print('Walking...')

    def __str__(self):
        return f'{super().__str__()}, and comes in at {self.weight} kg.'


class Fish(Animal):

    def swim(self):
        print('Swimming...')


# We created some instances to play with:

animal = Animal()

mammal = Mammal()
mammal.walk()

fish = Fish()
fish.swim()

try:
    # mammal.age = 4  # Also possible, uncomment to see what happens
    print(mammal.age)
except AttributeError:
    print('Fix this by uncommenting line 22')

print()  # for cleaner printout

# Because the constructor of the base class is executed, we still have have its attribute age value set to 10,
# we can still change that value like so:
mammal.age = 25


# Printout of our instances:

print(animal)
print(mammal)
print(fish)

# In recap:

# Method overwriting means replacing or extending a method defined in the Base class.
# We extended the constructor in this example. [which is of course a special method ;)]
