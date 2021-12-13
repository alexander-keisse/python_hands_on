# In terms of typing, programming languages fall into 2 categories:

# 1. Static typing; C++, C#, Java
# 2. Dynamic typing; JavaScript, Ruby, Python

# In a static language you would define a variable as so:
# int studentCount = 1;

# Once you declared the variable as of type int you can only use it to store int values,
# so the following piece of code would give a compilation error:

# studentCount = true;

# When using a dynamic language the type will be determined at runtime,
# and because of this mechanism a variable can change type.

# This is how to find out the type of a variable:

student_count = 1
print(type(student_count))

# Returns a type object

print(type(type(1)))

# Some examples of types in Python:

print(type(1.1))
print(type(True))
print(type(''))

# What if we change the type of value we store in student_count to a boolean:

student_count = True
print(type(student_count))  # Lets print again and check the result
