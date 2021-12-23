from pathlib import Path

# Makes sense:

new_line = '\n'

# When you wanna work with files and directories,
# you will need a Path object that represents where that file or directory lives.

# Here are 2 examples that show the difference between a Unix and a Windows folder hierarchy:

# Unix:         /home/elliot/Desktop/password.txt
# Find out more about the first forward slash in above path: https://www.makeuseof.com/tag/folders-linux-root-directory/

# Windows:      C:\Users\Mr Robot\Desktop\password.txt

# When creating a Path instance on windows we have 2 options:

# Because Windows uses a backslash as a separator we could use this notation [but not really, it is haaaard]:
windows_path_1 = Path('C:\\Downloads\\secret_vid.mp4')

# Here we are using a raw string, meaning \ is not an escape character, the value given is taken as is!
windows_path_2 = Path(r'C:\Downloads\secret_vid.mp4')

# If we dont know where we are in the current folder hierarchy,
# we can simply make an Path instance without giving it an argument during creation:

place_in_universe = Path()

# We can also combine Path objects with strings to form a new Path instance as such:

project = Path('/home') / 'eliot' / 'PycharmProjects' / 'python_basics'

# If you want to know the current home of the user you can use the following method:

home = Path.home()

# We will use the project variable to play around with, and see the most useful methods

# See if our path exists:

print(f"The path {project} exists: {project.exists()}{new_line}")

# Check if our instance is a file:

print(f"The path {project} is a file: {project.is_file()}{new_line}")

# Check if our instance is a directory:

print(f"The path {project} is a directory: {project.is_dir()}{new_line}")

# We can extract individual components in this path:

this_file = project / 'python-standard-lib/WorkingWithPaths.py'

print(this_file.name)  # Returns name of file at the end of our Path if no file found returns last directory

# We can also lose the file extension like so:

print(this_file.stem)

# If we want only the file extension:

print(this_file.suffix)

# If we only want the parent path:

print(this_file.parent)

# What if we want to modify our name and extension and store it as a new Path, beware this will not make a new file!

this_file_modified = this_file.with_name('not_a_virus_for_sure_homeboy.exe')
print(this_file_modified)

# If you need an absolute path:

print(this_file_modified.absolute())  # Doesn't mean that the file exist, this is only a representation of a path!!

# If you want to find out more about the pathlib module go here: https://docs.python.org/3/library/pathlib.html
