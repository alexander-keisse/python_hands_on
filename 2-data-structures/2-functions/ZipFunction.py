# We will make 2 lists to play around with:

products = ['Xiaomi Mi Electric Pro Scooter',
            'AMD Ryzen 7 3700X socket AM4 processor',
            'Bowers & Wilkins PX5 hoofdtelefoon',
            'Blue Microphones Yeti USB microfoon']

prices = [549, 359, 299, 129]

# If wanted to combine them in a single list holding Tuple values:
# taking the first element out of both list combine them in a Tuple, etc...:

# [(Xiaomi Mi Electric Pro Scooter, 549),
# (AMD Ryzen 7 3700X socket AM4 processor, 359),
# (Bowers & Wilkins PX5 hoofdtelefoon, 299),
# (Blue Microphones Yeti USB microfoon, 129)]

# We can't use the map function or list comprehension because both of those work only on a single list!
# Luckily for us the built in function zip exists [Takes multiple iterable objects as argument/s].

# Good practice guys:

msg_lists = 'Combined list created out of objects from same index out of 2 different lists:'
msg_iterables = 'Combined list created out of objects from same index out of 3 different iterables:'
new_line = '\n'

# You guessed it, this function returns a zip object so we need to cast to list:

list_combined_out_other_lists = list(zip(products, prices))
print(F'{msg_lists} {list_combined_out_other_lists}', new_line)

# We can do this with as many iterable objects as desired, beware will take the shortest iterable, loses other indexes:

list_combined_out_iterables = list(zip(products, prices, '123456'))
print(F'{msg_iterables} {list_combined_out_iterables}', new_line)
