# We will make a list holding Tuple variables and we only need the price[second value] from it:

items = [
    ('Product1', 27),
    ('Product2', 10),
    ('Product3', 42),
    ('Product4', 84),
    ('Product5', 14)
]

# here is the basic way to do it, not recommended:

prices = []
for item in items:
    prices.append(item[1])

# Print the result of our boring code:
print(prices)


# Now we are done with the boring way lets explore the built-in function map.
# Learn more at: https://docs.python.org/3/library/functions.html#map

# This is what we are giving to the map function: lambda parameter: expression, iterable object:

map_obj_only_prices = map(lambda single_item: single_item[1], items)

# Print out result of coowl code:
print(map_obj_only_prices)  # This behaviour comes from the fact that the map function returns a map object

# Cast to a list:

list_prices = list(map_obj_only_prices)

# Printout eh voila:
print(list_prices)
