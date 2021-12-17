# In many languages we are swapping values.
# Most C like languages take following approach:

x = 27
y = 42

z = x  # We need a dummy variable to store the value in whilst swapping
x = y
y = z

print('X:', x)
print('Y:', y)

# In Python we dont need a dummy variable:

numb1 = 10
numb2 = 11

numb1, numb2 = numb2, numb1  # left side are variables declared for unpacking | right side is actually a Tuple
# numb1, numb2 = (11, 10)  # This is the same as statement above  [you can also lose the (), still the same result!]

print('numb1:', numb1)
print('numb2:', numb2)
