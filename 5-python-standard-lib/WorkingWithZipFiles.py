from pathlib import Path
from zipfile import ZIP_DEFLATED
from zipfile import ZipFile
from time import sleep
import shutil

# Makes sense:

write = 'w'
new_line = '\n'

zipped_examples = './zipped-resources/test_pictures.zip'

# We create a Path instance so that we can later zip our python-standard-lib folder into a zipfile:

source = Path('../2-data-structures')

# We will need a path to place our target file as well.

target = './zipped-resources/data-structures.zip'

# Will create an empty zipfile in specified target, if file with the name exist it will be overwritten:

with ZipFile(target, write, ZIP_DEFLATED) as w_file:

    # This is how we can place our data in that zip file:
    for path in source.rglob("*.*"):
        if path.is_file():
            w_file.write(path)


# We can also read from our zipfile:

with ZipFile(target) as r_file:

    # We can collect all the names of the files stored in our zipfile into a list:
    name_files = r_file.namelist()
    print(f'list of all file names: {name_files}{new_line}')

    for name in name_files:
        # Here we get an object back holding info about our zipped file:
        info = r_file.getinfo(name)

        # And we can use that info object to show us the original and the compressed size:
        print(f"{name} -> Original size : {info.file_size} [bytes]")
        print(f"{name} -> Compressed size [bytes]: {info.compress_size} [bytes]{new_line}")

    # We can extract it to somewhere else:
    r_file.extractall("extracted-classes")

    sleep(60)  # This so you can inspect the folder before deletion

    try:
        shutil.rmtree('extracted-classes')
    except FileNotFoundError as e:
        print(e, '\n', 'Please remove extracted-classes manually')
    else:
        print('In order to keep this directory clean we removed the extracted folder.')
        print('In order to succeed we need to import the shutil module [because of the target folder not being empty]')
