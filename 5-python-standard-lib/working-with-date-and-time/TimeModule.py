import time
import random

# In this package you will learn how to work with date and time in Python

# In Python we have 2 modules to work with date and time and those are:

# 1. time module: this gives us a timestamp
# 2. datetime module: this one gives us date time objects with attributes like year, month, ...

# You probably guessed which one we will use here by taking a look at the class name :p

# Lets create our first timestamp:

timestamp = time.time()

# Our timestamp will be a floating point number holding the seconds since the epoch
# more info on the epoch can be found here: https://en.wikipedia.org/wiki/Unix_time
print(timestamp)


# Our timestamp is not really human readable so we will use this most often to make some sort of calculation.
# This could be used to time your execution time for example:

def send_emails_to_clients():
    for i in range(10):
        time.sleep(random.uniform(0.5, 1.5))


start = time.time()
send_emails_to_clients()
stop = time.time()

execution_time = stop - start

print(f"All emails were sent in: {execution_time} seconds.")
