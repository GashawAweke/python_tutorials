# An iterable is any object you can loop through.


# | Type       | Example            |
# | ---------- | ------------------ |
# | String     | `"python"`         |
# | List       | `[1, 2, 3]`        |
# | Tuple      | `(1, 2, 3)`        |
# | Set        | `{1, 2, 3}`        |
# | Dictionary | `{"name": "John"}` |
# | Range      | `range(10)`        |


# Iterating Over Strings
for character in "python":
    print(character)


# Iterating Over Lists
names = ["Alice", "Bob", "John"]

for name in names:
    print(name)


# Iterating Over Dictionaries

user = {
    "name": "Alice",
    "age": 25
}

for key in user:
    print(key)


# Keys and Values
for key, value in user.items():
    print(key, value)
