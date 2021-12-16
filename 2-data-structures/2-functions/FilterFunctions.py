# We need a list to work with:

items = [
    ('Product1', 8),
    ('Product2', 10),
    ('Product3', 2),
    ('Product4', 84),
    ('Product5', 4),
    ('Product6', 27),
    ('Product7', 42),
    ('Product8', 7),
    ('Product9', 19)
]

# Lets say you wanted all the products that the price is equal or less then 10:
# For this task we can use the built-in function filter:

# We use our expression side of the lambda to determine to criteria for filtering if true it returns that object:

list_cheap_products = list(filter(lambda item: item[1] <= 10, items))

# And now lets see the results:

print(list_cheap_products)

# We can also change the sorting order using the price of the item to go by:

list_cheap_products.sort(key=lambda item: item[1], reverse=True)

# Lets finish it:
print(F'{"Sorted list:"} {list_cheap_products}')
