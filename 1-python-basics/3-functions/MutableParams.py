# If you pass a variable as an argument, Python passes to the function the object [value] to which
# the variable currently refers, not the variable itself,
# and this value is bound to the parameter name in the function call namespace.


def f(x, y):
    x = 23
    y.append(42)


# Thus, a function can not rebind the caller's variables.
a = 77

# However, if you pass a mutable object as an argument,
# the function may request changes to that object,
# because Python passes the object itself, not a copy.
b = [99]

f(a, b)

# Print shows that a is still bound to 77 .
print(a, b)

# TL;DR:

# Function f ’s rebinding of its parameter x to 23 has no effect on f ’s caller,
# nor, in particular, on the binding of the caller’s variable that happened to be used to pass 77
# as the parameter’s value. However, print also shows that b is now bound to [99, 42].

# b is still bound to the same list object as before the call,
# but that object has mutated, as f has appended 42 to that list object.

# In either case, f has not altered the caller’s bindings, nor can f alter the number 77,
# since numbers are immutable. However, f can alter a list object, since list objects are mutable.
