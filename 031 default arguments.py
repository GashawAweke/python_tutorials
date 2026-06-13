# Default arguments make parameters optional.


def increment(number, by=1):
    return number + by


print(increment(2))


# Overriding the Default
print(increment(2, 5))


# Multiple Defaults
def connect(host="localhost", port=5432):
    print(host, port)


connect()
connect("db.company.com")
connect(port=3306)


# Important Rule

# Required parameters must come before optional parameters.

# Correct:


def create_user(name, age=18):
    pass
# In Python, pass is a null placeholder keyword. It tells the interpreter to do nothing. It is primarily used when you need a function or class defined in your code to avoid syntax errors, but you aren't ready to write the actual logic yet.


# Wrong:

def create_user(age=18, name):
    pass
# Error: SyntaxError
