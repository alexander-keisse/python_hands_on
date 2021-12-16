# In the Stacks.py file we are using the LIFO principle,
# but here we will be using the FIFO principle [First In First Out]

# For this we will not be using a list as this would be too cpu expensive
# Explanation for this:

# If you have lets say a list with 1001 items
# and you would remove the first index you would have to move a 1000 values to the left in your list

# We will simulate a food stand here.
# The first in line gets his food first, then the second person is served and etc...

from collections import deque

# Makes sense:

new_line = '\n'

# instead of making a list we will use deque from the collections module[more on modules later]:

waiting_queue = deque([])

# Make some strings representing humans:

kenan = 'Kenan'
bart = 'Bart'
wouter = 'Wouter'
patrick = 'Patrick'
olmo = 'Olmo'
alex = 'Alex'

# We can add some values as such:

waiting_queue.append(kenan)
waiting_queue.append(bart)
waiting_queue.append(wouter)
waiting_queue.append(patrick)
waiting_queue.append(olmo)
waiting_queue.append(alex)

# Lets see what we have in our queue:

print(F'{"Waiting line:"} {waiting_queue}', new_line)

# Okay lets shorten our waiting_queue by removing the first customer:

first_served = waiting_queue.popleft()  # This method is not available with lists
print(F'{"Served:"} {first_served}', new_line)

# Lets take a look at our waiting queue again:

print(F'{"Waiting line:"} {waiting_queue}', new_line)

# Lets work down our queue and serve all those hungry people:

for person in range(len(waiting_queue)):
    if waiting_queue:
        print(F'{"Served:"} {waiting_queue.popleft()}', new_line)
        print(F'{"Waiting line:"} {waiting_queue}', new_line)

# Go back to ForElse.py if this doesn't make any sense
else:
    print('All done for the day!')
