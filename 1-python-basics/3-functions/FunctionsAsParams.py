def shout(text):
    return text.upper()


print(shout("Hello"))

yell = shout
print(yell("Hello"))


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("Hi, I am created by a function passed as an argument.")
    print(greeting)


greet(shout)
greet(whisper)


def hello_decorator(func):

    # inner1 is a Wrapper function in which the argument is called

    # inner function can access the outer local functions like in this case "func"

    def inner1():
        print("Hello, this is before function execution")

        # Calling the actual function now inside the wrapper function
        func()

        print("This is after function execution")

    return inner1


def function_to_be_used():
    print("This is inside the function !!")


function_to_be_used = hello_decorator(function_to_be_used)

function_to_be_used()