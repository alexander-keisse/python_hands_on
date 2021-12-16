# What if we have a list of Tuples and want to sort them,
# You are writing a program for processing orders:

# Lets start by making a list holding Tuple values:

items = [
    # Every item in this list is a tuple containing 2 values:
    # 1. Product name 2. Price
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 18),
    ('Product4', 42),
    ('Product5', 27),
    ('Product6', 29),
    ('Product7', 4)
]

# What would happen if we used the sort method here:

items.sort()

# Why dont we take a look:

print(items, '\n')  # Nothing is changed, Python doesn't know what to do with the list


# A way of helping Python is giving it a value that is sortable,
# We can make a function to do that:

def sort_item(item):
    return item[1]  # Location of the price in our tuple, Python knows how to sort numbers


# Now we can use the sort method again:

items.sort(key=sort_item)  # Our function is passed to the keyword argument key

# Lets see what our friend Python could with a little help:

print(items)
