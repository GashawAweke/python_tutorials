# Tuples

# A tuple is an ordered, immutable collection.


coordinates = (10, 20)

print(coordinates[0])  # 10


# Why tuples exist

# Use tuples when data should not change.

# Examples:

# GPS coordinates
# Database records
# RGB colors
# Configuration values


rgb_color = (255, 0, 0)

server = ("192.168.1.10", 443)


# Single item tuple

# Wrong:

item = (10)
print(type(item))
# int

# Correct:

item = (10,)
print(type(item))
# tuple


# Tuple unpacking

user = ("John", 25)

name, age = user

print(name)
print(age)


# Returning multiple values from functions

# Very common in real projects.


def get_user():
    return "John", 25


name, age = get_user()
