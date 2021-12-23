# In this class we will make a good example of inheritance.

# We will make a base class for working with streams.
# We can read a stream of data from multiple sources and every source is different to read:

# File stream
# Network stream
# Memory stream

# They all have behaviour in common:

# We can:

# Open
# Close
# Read data

# Reading data from our different sources will every time be handled in a different way

# In this example we will also write our own Exception class,
# this to make sure that we can raise an exception if we try and do an invalid operation with our stream:


class InvalidOperationError(Exception):  # If writing our own Exception we mostly use the Exception as a base class.

    pass


class Stream:  # Our base class, from here we inherited all our wanted default behaviour for our sub classes.

    def __init__(self):
        self.opened = False  # Flag used to see if our stream is already open, default false.

    def open(self):
        if self.opened:
            raise InvalidOperationError('Stream is already open!')
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError('Stream is already closed!')
        self.opened = False


class FileStream(Stream):

    # For simplicity we will only do a printout in our examples
    def read(self):
        print('Reading data from a file...')


class NetworkStream(Stream):

    # For simplicity we will only do a printout in our examples
    def read(self):
        print('Reading data from a network...')


class MemoryStream(Stream):

    # For simplicity we will only do a printout in our examples
    def read(self):
        print('Reading data from memory...')


# Like you can see we don't really have multi-level inheritance, you could at max add 1 level more. [for good practices]
# We avoided multiple inheritance our classes have only 1 base class, try to avoid multiple inheritance when possible
