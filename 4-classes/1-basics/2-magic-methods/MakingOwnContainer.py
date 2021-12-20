from random import choice

# Makes sense:

new_line = '\n'

tag_low_python = 'python'
tag_low_java = 'java'
tag_low_c = 'c'
tag_low_vb = 'visual basic'
tag_low_cobol = 'cobol'
tag_low_js = 'javascript'

tag_upper_python = 'Python'
tag_upper_java = 'Java'
tag_upper_c = 'C'
tag_upper_vb = 'Visual Basic'
tag_upper_cobol = 'COBOL'
tag_upper_js = 'JavaScript'

programming_languages = [tag_low_python, tag_low_java, tag_low_c, tag_low_cobol, tag_low_vb, tag_low_js
                         , tag_upper_python, tag_upper_java, tag_upper_c, tag_upper_cobol, tag_upper_vb, tag_upper_js]

# We have already worked with: Lists, Sets, Dictionaries and so on.
# We can actually go a step further and create a custom data class [usefulness depends on the situation].

# In this example we will create such a data class, so store tags and keep count. [useful in regards to a blog site]


class TagCloud:
    # We will use a dictionary object, because of its key-value character.
    def __init__(self):
        self.tags = {}

    # Do a check if the tag is already stored, if so we add to the value of our dictionary.
    # If key not already there, we set the key and give it value of 1.
    def add(self, tag):
        tag = tag.lower()
        self.tags[tag] = self.tags.get(tag, 0) + 1

    def __getitem__(self, item):
        item = item.lower()
        return self.tags.get(item)

    def __setitem__(self, key, count):
        self.tags[key.lower()] = count

    def __len__(self):
        return len(self.tags)

    # This method will return an iterable object,
    # this makes iterating our container class possible like seen on line 84
    def __iter__(self):
        return iter(self.tags)

    def __str__(self):
        return str(self.tags)


# Creating a cloud instance to play with:

cloud = TagCloud()

# Automated filling with different programming language tags:

for i in range(100):
    cloud.add(choice(programming_languages))

# Printout to check if instance does what is expected:
print(cloud, new_line)

# This can be very useful to do, to achieve this you need to implement the magic method __getitem__:
print(f"{tag_upper_python} occurred: {cloud[tag_upper_python]} times.")

# We of course would like to boost the numbers of python refs, and we can do that like so:

cloud[tag_upper_python] = 420  # this is possible after overwriting the magic method __setitems__
print(f"{tag_upper_python} occurred: {cloud[tag_upper_python]} times.{new_line}")  # lets see our fraud results :p

# If you want to be able to see how many key-value pairs our cloud object holds using the len method,
# we need to give our magic method __len__ a new implementation.
print(f"Cloud holds {len(cloud)} key-value pairs.{new_line}")

# If we want to iterate over an instance of our container class we only need to give the magic method
# __iter__ a new implementation:
for key in cloud:
    print(f"key: {key}, value: {cloud[key]}")
