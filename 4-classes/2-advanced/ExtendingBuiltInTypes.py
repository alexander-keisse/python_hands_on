# In Python we can fairly easy extend all sort of Built-in Types.

# This is of course very powerful and can be done for a number of reasons:

# We could make some own implementations for certain methods of the base class.
# We can add certain methods that we're not needed for the base class, but would be very useful in our sub class.

# We will make 2 examples showing this:

# We start with a class called Text it will extend the build-in type str:


class Text(str):

    # We inherit all methods from the str class and add our own method to duplicate a text object:
    def duplicate(self):
        return self + self  # concatenating str with itself


# We make some objects to play with:

text = Text("Elliot")

# Printout:

print(text.lower())  # We still have access to all string methods
print(text.duplicate(), '\n')


# We make a second example, we make our own list that notifies us if the list grows using the append method

class NotifierList(list):

    def append(self, item):
        print('List is ever growing master, append has been used!')
        super(NotifierList, self).append(item)


# We make some objects to play with:

list_ntf = NotifierList()

# Playtime:

for n in range(20):
    list_ntf.append('foo')
    list_ntf.append('bar')
else:
    print()

print(*list_ntf)
