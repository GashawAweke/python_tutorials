# Dictionaries
# Most important data structure after lists.
# Stores key-value pairs.


# Stores key-value pairs.


user = {
    "name": "John",
    "age": 25,
    "is_admin": True
}


# Access values
print(user["name"])


# Add values

user['email'] = 'john@mail.com'

print(user)


# Update values
user['age'] = 26

print(user)


# Delete values


del user['age']

print(user)

# print(user['age'])

# Safe access
# Avoids KeyError.

age = user.get("age")

print(age)


# With default value:

age = user.get("age", 0)


# Looping through dictionaries

for key, value in user.items():
    print(key, value)
