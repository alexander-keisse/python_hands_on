import json
from pathlib import Path

# Makes sense:

mov_id = 'id'
title = 'title'
rel_year = 'release year'
json_file = Path('./json-files/movies.json')
json_file_nottingham = Path('./json-files/opendatanottingham.json')
new_line = '\n'

# We are going to take a look at JavaScript Object Notation better known as JSON.
# This is a very popular way to describe data in a human readable way, A lot of website use this to represent their data

# We will start by making an array called movies that holds dictionaries describing a movie:

movies = [
    {mov_id: 1, title: 'Lucy', rel_year: 2014},
    {mov_id: 2, title: 'Interstellar', rel_year: 2014},
    {mov_id: 3, title: 'Transcendence', rel_year: 2014},
    {mov_id: 4, title: 'Inception', rel_year: 2010},
    {mov_id: 5, title: 'Shutter Island', rel_year: 2010}
]

# We can convert this data into JSON and store that into a variable like so:

data = json.dumps(movies)

# When we do the printout beneath you can see this happens to be the same like we defined it in Python,
# but beware that this will not be the case for all programming languages!

print(data, new_line)

# Instead of printing this to our terminal its more useful to write this data to a json file:

json_file.write_text(data)

# We can also take a json file and convert that to an Python object of course:

data = json_file_nottingham.read_text()  # data is a string containing our data[movies] as a json string representation.

# Deserialize ``s`` (a ``str``, ``bytes`` or ``bytearray`` instance containing a JSON document) to a Python object:

fines = json.loads(data)  # Will convert into a list holding our dictionary values

# Lets printout some useful details of our fines:
for fine in fines:
    print(f"Offense: {fine.get('Contravention_Description')}{new_line}"
          f"Amount of fine: {fine.get('Amount_Paid(£)')}{new_line}"
          f"Status: {fine.get('Status')}{new_line}")
