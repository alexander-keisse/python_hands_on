# List comprehension is something not found in other languages
# First lets look back on how we filtered and mapped our lists:

# Makes sense:

new_line = '\n'
items = [
    ('Product1', 188),
    ('Product2', 147),
    ('Product3', 141),
    ('Product4', 8),
    ('Product5', 15),
    ('Product6', 66),
    ('Product7', 87),
    ('Product8', 45)
]

# Strings to display message about what is user seeing:

mapped_list_message = "[using built-in map function] | Prices of every product in our items list:"
filter_list_message = "[using built-in filter function] | Filtered list of products that cost equal or less then 50:"
list_comprehension_message_map = "[using list comprehension] | Prices of every product in our items list:"
list_comprehension_message_filter = "[using list comprehension] | All products with cost 50 or less in our items list:"

# Showing the builtin functions map and filter | printing output:

list_prices = list(map(lambda item: item[1], items))
print(F'{mapped_list_message} {list_prices}', new_line)

filtered_list = list(filter(lambda item: item[1] <= 50, items))
print(F'{filter_list_message} {filtered_list}', new_line)

# Now lets see how we can achieve the same result using list comprehension [good practice in Python].
# Lets first look at the basic syntax of list comprehension:

# [expression for item in items]  # The last part of this syntax we're actually quite familiar with a for loop

# Now lets try and "map" all prices in our items list using this list comprehension:

list_prices_list_comprehension = [item[1] for item in items]
print(F'{list_comprehension_message_map} {list_prices_list_comprehension}', new_line)  # Printout the result

# And filtering can be done like this:

list_filtered_products = [item for item in items if item[1] <= 50]
print(F'{list_comprehension_message_filter} {list_filtered_products}', new_line)  # Printout the result
