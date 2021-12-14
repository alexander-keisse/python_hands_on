def my_func(arg1, arg2, arg3):
    print("arg1", arg1)
    print("arg2", arg2)
    print("arg3", arg3)


# Now we can use *ars or **kwargs to pass arguments to this function:

args = ("Geeks", "for", "Geeks")
kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}

print(type(args))
my_func(*args)

print(type(kwargs))
my_func(**kwargs)
