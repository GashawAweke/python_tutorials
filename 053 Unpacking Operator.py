# Unpacking Operator(* and **)

# One of Python's most powerful features.


# List Unpacking(*)
numbers = [1, 2, 3]

a, b, c = numbers


# Capture remaining values
numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print(first)
print(middle)
print(last)


# Merge lists
a = [1, 2]
b = [3, 4]

combined = [*a, *b]


# Dictionary Unpacking(**)

# Merge dictionaries.


user = {
    "name": "John"
}

details = {
    "age": 25
}

combined = {
    **user,
    **details
}


# Overriding values:The later dictionary wins.
default_settings = {
    "theme": "light"
}

user_settings = {
    "theme": "dark"
}

settings = {
    **default_settings,
    **user_settings
}


# passing function arguments
def create_user(name, age):
    print(name, age)


data = {
    "name": "John",
    "age": 25
}

create_user(**data)
