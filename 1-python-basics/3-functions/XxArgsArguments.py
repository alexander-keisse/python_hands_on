# Lets simulate some db action with python 3.7 :D

# We can write a function for that:

# Instead of giving it an arbitrary amount of arguments,
# we use an arbitrary amount of keyword arguments.

# let me google that for you: https://duckduckgo.com/?q=python+keyword+arguments&atb=v120-7&ia=web


def save_user(**user):
    print(f'user saved: {user}')
    if user['name']:
        print(user['name'])


save_user(id=1, name='Admin')  # printout holds a key/value pair


# The printout from above is actually a Python dictionary
# JS devs should recognize this format it looks like an object in JavaScript
