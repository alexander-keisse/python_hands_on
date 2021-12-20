# There are times in programming where we want full control over our attributes.

# In this example we create a Product class,
# its important that when we create an instance of this class and that our price can't be negative:


class Product:

    def __init__(self, price):
        self.price = price
        # Uncomment after you reached line 32:

        # self.set_price(price)  # This implementation works, but is not Pythonic! [correct way is on line 14]
        # self.__price = price  # This to make a "private" attribute

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative!')
        self.__price = value

    price = property(get_price, set_price)


# Lets create a product with a positive price:

product = Product(42)

# We will hack the price and set it to a negative value, so they pay us for buying this product:

try:
    product.price = -25  # Let's see if they secured their class...
except ValueError as ve:
    print(ve)

print(product.price)  # Prints the result

# It seems that they have adapted their system, we must find another way
product.set_price(0)
print(f'Okay, at least it is a free product then: {product.price}')

# Now let us make another class to show how to deal with this in the correct way, and securing our constructor as well:
# This approach lets us use name as a real property of the class.


class Human:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    # You could even drop this setter if you want a read only property meaning:

    # After initialising an object of this class,
    # you will no longer be able to change it using: elliot.name = 'Diff name' syntax [If tried => AttributeError].
    @name.setter
    def name(self, name):
        if name == '':
            raise ValueError('A name can not be empty!')
        self.__name = name

    def __str__(self):
        return self.__name


# Create an instance to play with:

elliot = Human('Elliot')

try:
    elliot = Human('')
    # elliot.name = ''  # This is now also protected.
except ValueError as ve:
    print(ve)

# We can use this like a regular attribute:
print(f"Name of the human: {elliot.name}")
