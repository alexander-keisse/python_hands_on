# Makes sense:

new_line = '\n'

out_surname = 'Elliot'
out_name = 'Anderson'

answer_to_everything = 42
teenager_iq = 16

# Sometimes its useful to compare objects and see if they are actually the same instance


class Point:

    default_col = 'red'

    def __init__(self, x, y, z):  # Magic method
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):  # Magic method
        return f'Point ({self.x}, {self.y}, {self.z})'

    @classmethod
    def zero(cls):
        return cls(0, 0, 0)


# We are gonna make 2 instances holding the same value and compare them with the equal operator:
first_point = Point(18, 42, 27)
sec_point = Point(18, 42, 27)

print(f'Objects are the same: {first_point == sec_point}{new_line}')

# A smart thing to do is use our id function to lookup their memory address:
print(f'first_point memory address: {id(first_point)}')
print(f'id sec_point memory address: {id(sec_point)}{new_line}')


# We will make a second class to see how we can fix this [and changing the class we work with keeps it fun ;)]
class Human:

    def __init__(self, surname, name, intelligence):
        self.surname = surname
        self.name = name
        self.intelligence = intelligence

    def __str__(self):
        return f'{self.surname} {self.name}'

    # We can overwrite the default behaviour when using the equal operator:
    # compare value of the instance instead of the memory address
    def __eq__(self, other):
        return self.surname == other.surname and self.name == other.name

    # We can also overwrite the greater then operator, in order to succeed:
    def __gt__(self, other):
        return self.intelligence > other.intelligence


# We make some objects [pun intended]:

first_human = Human(out_surname, out_name, answer_to_everything)
sec_human = Human(out_surname, out_name, teenager_iq)

# Put the magic method __eq__ in comment, run the program again to see the diff:

print(f'Human 1 and human 2 are the same object: {first_human == sec_human}')
print(f'Human 1 is more advanced then human 2: {first_human > sec_human}{new_line}')

print(f'Human 1 memory address: {id(first_human)}')
print(f'Human 2 memory address: {id(sec_human)}')
