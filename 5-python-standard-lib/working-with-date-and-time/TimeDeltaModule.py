from datetime import datetime, timedelta

# Makes sense:

new_line = '\n'

# timedelta module is used to represent a duration in time and lets us easily play around with datetime objects

# Lets create 2 different datetime objects to play with:

dt1 = datetime(1989, 3, 16)
dt2 = datetime.now()

# To calculate the duration in time we simply do the following:

duration = dt2 - dt1

# Lets take a look at the result:
print(duration, new_line)

# We can use some handy attributes:
print(f"Days past since birth: {duration.days}")
print(f"Duration fully converted into seconds: {duration.total_seconds()}{new_line}")

# Okay, okay enough about datetime objects show me the use of the timedelta module:

tomorrow = dt2 + timedelta(days=1)  # You can also do this with: seconds, microseconds, milliseconds, hours, minutes

# Lets see what we get:
print(f"tomorrow's date is: {tomorrow.day}/{tomorrow.month}/{tomorrow.year}")
