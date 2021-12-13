# You know the drill make a variable to play with:

age = 22

# Lets take a look at this simple if else construction:

if age >= 18:
    message = 'Eligible'
else:
    message = 'Not eligible'

# Either way what happens above we print out a message:

print(message)

# Lets look at the Java way:
# String message = age >= 18 ? "Eligible" : "Not eligible";

# And now the Python way (the Python can screw up to, you know):

message = 'Eligible' if age >= 18 else 'Not eligible'
print(message)
