from pathlib import Path
from timeit import timeit

# Makes sense:

new_line = '\n'

# In this class we will be working with directories hence the name of the class.
# I will be going over the most used methods, so lets dive in to the code:

# First we will need a Path object that represents a directory:

path_python_std_lib_dir = Path('../5-python-standard-lib/')
path_new_dir = path_python_std_lib_dir / 'resources/'

# If you want to see if a certain directory exist you can do it like this:

print(f"The path {path_python_std_lib_dir} is a directory that exists: {path_python_std_lib_dir.exists()}{new_line}")
print(f"The path {path_new_dir} is a directory that exists: {path_new_dir.exists()}{new_line}")

# Lets create a new directory:

try:
    path_new_dir.mkdir()
except FileExistsError as fee:
    print(fee)
else:
    print(f'{path_new_dir} is created.')

# Lets delete it right away like this:

try:
    path_new_dir.rmdir()
except FileNotFoundError as fnfe:
    print(fnfe)
else:
    print(f'{path_new_dir} has been removed.')

# If you want to rename it you can do like so:

try:
    path_new_dir.mkdir()  # Create a directory to rename
    path_new_dir.rename('test_renaming')  # Rename the directory
    path_new_dir = Path('./test_renaming')  # Store the new path
    path_new_dir.rmdir()  # delete the directory to keep it clean
except (FileExistsError, FileNotFoundError) as io_error:
    print(io_error)

# One of the more useful and interesting methods is the iterdir method that returns a generator object containing
# all files and subdirectories of our directory represented by the path object.

iter_dir = path_python_std_lib_dir.iterdir()

# So now we can iterate over it:

for i in iter_dir:
    print(i)
else:
    print()

# Now if your directory is not to big you could put it in a list,
# this can be handy if you wanna work with it in the future:

list_dir_cont = [p for p in path_python_std_lib_dir.iterdir()]

# We actually have 2 kind of paths: PosixPath and WindowsPath [i'm working on linux, so I get a PosixPath]
print(list_dir_cont)

# We can even do filtering on this list comprehension:

files_in_dir = [p for p in list_dir_cont if p.is_file()]
sub_dirs_in_dir = [p for p in list_dir_cont if p.is_dir()]

# And this way you can recursively search for a certain pattern in a directory, in our case we look for all python
# related files.

# Let's take a look at the difference between a list[code1] and an generator object[code 2]:

list_object = """
from pathlib import Path

path_home = Path.home()
py_files = [p for p in path_home.rglob('*.py')]

"""

generator_object = """
from pathlib import Path

path_home = Path.home()
py_files = (p for p in path_home.rglob('*.py'))

"""

alternative_gen_obj = """
from pathlib import Path

path_home = Path.home()
py_files = (p for p in path_home.rglob('*.py'))

for key, value in enumerate(py_files):
    print(key, " ",value)

"""

try:
    print('Execution time of our code using list: ', timeit(list_object, number=20))
    print('Execution time of our code using generator object: ', timeit(generator_object, number=20))
    # print('Execution time of our code using generator object: ', timeit(alternative_gen_obj, number=1))
except KeyboardInterrupt as ki:
    print(ki)
