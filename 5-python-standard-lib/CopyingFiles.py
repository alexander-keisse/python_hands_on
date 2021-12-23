from pathlib import Path
import shutil

# In this class I will show you how to copy files from a certain source to a chosen target:

source = Path('./txt-files/Intro.txt')

# We make 2 different Path objects to play with, one exist to other will be used to create a new file:

target_must_exist = Path('./copy-txt-files/BlankIntro.txt')
target_will_be_created = Path('./copy-txt-files/CopyIntro.txt')

# First way to copy the file, bit tedious:

target_must_exist.write_text(source.read_text())

# The second way is cleaner and if the file already exist the content will be update to that of the source file,
# if it doesn't exist the file will be created!

shutil.copy(source, target_will_be_created)
