# Question:

# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also, please include simple test function to test the class methods.

# Hints:
# Use init method to construct some parameters

class IOString:
    def __init__(self):
        self.string = None

    def get_string(self):
        self.string = input()

    def print_string(self):
        print(self.string.upper())


string = IOString()
string.get_string()
string.print_string()
