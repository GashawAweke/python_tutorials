# syntax :

# def greet():
#     print("Hi there")
#     print("Welcome aboard")


# Functions are reusable blocks of code that perform a specific task.


# Naming Conventions

# Use:

# lowercase letters
# underscores between words
# descriptive names


# Arguments and Parameters
# Parameter:
# The variable defined inside the function.

# Argument:
# The actual value passed to the function.


def greet(first_name, last_name):   # Parameters
    print(f"Hi {first_name} {last_name}")


greet("John", "Smith")              # Arguments


# Required Parameters

# By default all parameters are required.
# def: The keyword used to declare a function.

def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")


greet("John")  # TypeError: missing required positional argument


# Functions Return None by Default
def greet(name):
    print(f"Hi {name}")


result = greet("John")

print(result)
