# Lets make a definition to play with:


def grow(data=[]):
    data.append('?')
    return data


# Mind blown:

print(grow(list()))
print(grow())
print(grow())

# Python’s handling of default parameter values is
# one of a few things that tends to trip up most new Python programmers [usually only once]

# What causes the confusion is the behaviour you get when you use a “mutable” object
# as a default value; that is, a value that can be modified in place, like a list or a dictionary.

# As you can see, the list keeps getting longer and longer.
# If you look at the list identity, you’ll see that the function keeps returning the same object:

print(grow(), id(grow()))
print(grow(), id(grow()))
print(grow(), id(grow()))  # Yeah this print function I like it :)


# Workaround, as even suggested by the IDE:


def grow_workaround(data=None):
    if data is None:
        data = []
    data.append('?')
    return data


print(grow_workaround(), id(grow_workaround()))
print(grow_workaround(), id(grow_workaround()))
print(grow_workaround(), id(grow_workaround()))

# TL;DR
# Wanna know more google it: http://effbot.org/zone/default-values.htm
