from abc import ABC, abstractmethod

# Polymorphism is based on the greek words Poly (many) and morphism (forms).
# We will create a structure that can take or use many forms of objects.


class UIControl(ABC):

    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):

    def draw(self):
        print('TextBox')


class DropDownList(UIControl):

    def draw(self):
        print('DropDownList')


# We will write a function draw that takes an instance of different classes and uses its draw method:

def draw_single(control):
    control.draw()  # Python only knows at runtime which kind of object it's getting, polymorphism baby...


# Does the same as function above but takes a list holding different UIControl subclasses.

def draw_multi(controls):
    for control in controls:
        control.draw()


# Lets make some instances:

text_box = TextBox()
drop_down_list = DropDownList()

list_ui = [text_box, drop_down_list]

# Lets test polymorphism out:

draw_single(text_box)
draw_single(drop_down_list)

print()  # Cleaner print out.

draw_multi(list_ui)
