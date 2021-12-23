# We continue with the example from the AbstractBaseClass.py,
# Because python is a dynamically typed language we could leave out the UIControl base class.

# This behaviour is possible because of duck typing:

# If it walks like a duck and quacks like a duck then it's a duck according to Pythons rules.


class TextBox:

    def draw(self):
        print('TextBox')


class DropDownList:

    def draw(self):
        print('DropDownList')


# This example will work because we never declared that our param should be of type ...

def draw_single(control):

    # We achieve polymorphic behaviour here, according to the control object we will execute the appropriate method!
    control.draw()


# We can pass any kind of object as argument of these functions,
# here it needs to be iterable because of the for loop, but other then that Python won't give us a hassle.

def draw_multi(controls):
    for control in controls:  # controls need to be an iterable

        # Good programmers should see red flags in the code beneath. [we never check if the method exists]
        control.draw()  # If the argument we passed has a draw method, all is well.


# Lets make some instances to play with:

tb = TextBox()
ddl = DropDownList()

list_ui = [tb, ddl]

# Duck typing in action:

draw_single(tb)
draw_single(ddl)

print()

draw_multi(list_ui)
