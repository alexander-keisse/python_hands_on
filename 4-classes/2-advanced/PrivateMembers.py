# We have created our own container class, but there are still some issues with it.
# The biggest flaw being that we can directly access our tags dictionary.

# This is dangerous because it makes unmeant behavior and manipulation
# of that dictionary possible from outside our class.

# We will continue with this class and hide our tags dictionary outside the class:


class TagCloud:

    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        tag = tag.lower()
        self.__tags[tag] = self.__tags.get(tag, 0) + 1  # See the MakingOwnContainer.py file if this confuses you.

    def __getitem__(self, item):
        item = item.lower()
        return self.__tags.get(item)

    def __setitem__(self, key, count):
        self.__tags[key.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

    def __str__(self):
        return str(self.__tags)


# We make an object to see if we can still access our tags dictionary directly:

cloud = TagCloud()

# Lets try and print this tags attribute:
try:
    print(cloud.tags)
except AttributeError as ae:
    print(ae)

# We actually can still get access to this attribute, so hiding it is more for warning purposes then security:
print(f"All the attributes from our CloudTag instance: {cloud.__dict__}")

# Now lets hack our way in and change the data in our favour:
cloud._TagCloud__tags['Python'] = 8001

# This proves that unlike in other certain languages like: Java, C#, ... we don't really have private members.
# So the use of __ underscores is more a convention to help preventing accidental access to members,
# where its actually not preferable.
print(cloud)
