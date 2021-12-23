import time
from datetime import datetime

# Makes sense:

new_line = '\n'

# We will be working with datetime these are more readable then the timestamps,
# Most often used to represent a certain date to users.

# Lets take a look and see how we can create such objects:

dt = datetime(2017, 11, 8)

# printout of our date
print(f"Life changing moment: {dt}{new_line}")

# We can also create an object that represent current moment:

now = datetime.now()

# printout of current time
print(f"Time: {now}{new_line}")

# We can also parse a string to represent a datetime object.
# This can be very handy when converting user input or time we take out of a document.

# In order to do this we give it the string to parse, and tell it how to parse this string as seen below.

# You dont need to know the exact formatters you can find them here:
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

lucy = datetime.strptime("25/07/2014", "%d/%m/%Y")

# printout release date awesome movie:
print(f"Time is the only true unit of measure. It gives proof to the existence of matter. "
      f"Without time, we don't exist: {lucy}{new_line}")

# We can also convert a datetime object:

now = datetime.fromtimestamp(time.time())

# printout of current time
print(f"Time: {now}{new_line}")

# datetime objects also have attributes like day, month, year and so on:
print(f"Lucy came out in the year: {lucy.year}{new_line}")

# Or you could do this:
print(f"Current date: {now.day}/{now.month}/{now.year}{new_line}")
print('Current date:', now.strftime('%Y/%m/%d'), new_line)  # How ugly right xD?

# You can also compare dates:
print(F"Lucy was released before today: {lucy < now}")
