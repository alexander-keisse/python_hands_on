import subprocess

# Makes sense:

new_line = '\n'

# In this class we will take a look at how to run an external program.
# This could be very handy when making automation scripts.

# We need the subprocess module, this will allow us to create a child process [This way we can 1-start another program].
# A process can be seen as an instance of a running program...

# You might come across one of the following ways to use the subprocess, these are considered legacy:

# subprocess.call()
# subprocess.check_call()
# subprocess.check_output()
# subprocess.Popen

# These helper methods are used to create a new process, but the good practice is to use the following:

# subprocess.run()

# We will 1-start with an easy example in Linux we have the 'ls' command [dir on Windows]
# for listing the content of a directory. We can use this command from our python code and store the result it returns

subprocess.run(['ls', '-l', '-a'])
print()  # For cleanness in printout

# Lets take a look at the return value of this method

result = subprocess.run(['ls', '-l'])
print(f"{new_line}Type of the result variable: {type(result)}{new_line}")

# We can get allot of information out this instance:

print(f"args: {result.args}")
print(f"return code: {result.returncode}")
print(f"standard error: {result.stderr}")
print(f"standard output: {result.stdout}{new_line}")

# The default behaviour of our run method is to print the output to the console.
# However we can decide to capture this output, in some cases we want to do something with it:

# We can use the keyword argument to capture the output as a bytestream, like so:

completed = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)

# We can access this output then trough the attribute stdout:
print(f"standard output: {completed.stdout}{new_line}")

# We can simply convert the byte object to a string:

text = completed.stdout.decode('utf-8')

# Lets check if everything went as expected and instead of a byte object we have a string now
print(f"Byte object converted to string: {new_line}{text}")

# Uncomment beneath code to see another python program come into action:

# subprocess.run(['python3', 'CodeWithMosh.py'])

# If we are not sure, if our code will complete or just as a good practice do:

failing_process = subprocess.run(['false'])  # This won't work so our exit code will be 1

if failing_process.returncode != 0:
    print('Process did not complete correctly! Do something about it noob :D')
