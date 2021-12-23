from pathlib import Path
from time import ctime, sleep

# Makes sense:

new_line = '\n'
file_name = 'original.txt'
copy = Path('copy-txt-files/BlankIntro.txt')
new_file_name = file_name.capitalize()  # A good programmer is a lazy programmer :D

# In this class we will look at the handy methods to handle files with Python:

path = Path('txt-files')
txt_file = path / file_name  # Check WorkingWithPaths.py if this makes no sense ;)

txt_files = [p for p in Path().rglob('*.txt')]


def show_stats(files):
    for f in files:
        print(f"The file {f.name} exists {f.exists()}")  # This method checks if the file exists
        print(f.stat(), new_line)  # info about returned values see: https://docs.python.org/3/library/os.html#os.stat


# We can use this handy function, to get info about our files and see if it exists:

show_stats(txt_files)

# If we want to see the creation time we could do this as follows [from time import ctime]:

print(f"Time of creation: {ctime(txt_file.stat().st_ctime)}{new_line}")  # ctime function converts seconds from epoch

# Renaming a file:

print(f"Renaming: {txt_file}, new name: {new_file_name}")
txt_file.rename(new_file_name)  # Sloppy programming, to demonstrate pitfalls.
print('Renaming is done...', new_line)

sleep(5)  # In order to see the changes happening live...
txt_file = Path(new_file_name)  # Updated our path variable

# Remove this file or link, write content to new file first.
# If the path is a directory, use rmdir() instead to remove.

try:
    life_saver = path / file_name
    life_saver.touch()
    sleep(10)
    life_saver.write_bytes(txt_file.read_bytes())
    sleep(10)
    txt_file.unlink()
except FileNotFoundError as fnf:
    print(fnf, ' -> ', txt_file.name)


# TL;DR: Bonus part, explanation of the write_text and read_text functions

# Lets create a new path obj pointing to a text file:

intro_file = path / 'Intro.txt'

# We can also read the file as a byte object for representing the binary data:

byte_stream = intro_file.read_bytes()  # returns content as a byte object

# Let's see what we get as a result:
print(f"Byte object: {byte_stream}{new_line}")

# We can read the content of a file with the read_text function [returns the content as a string]:
print(f"Content of the file: {new_line}{intro_file.read_text()}{new_line}")

# All this is handled inside the read_text method for us:

# with open(intro_file, 'r') as file:
#     line = file.readline()
#
#     while line:
#         print(line)
#         line = file.readline()

# We can also write to a file as such:

copy.write_text(intro_file.read_text())
