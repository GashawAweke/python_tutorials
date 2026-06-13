# JSON(JavaScript Object Notation) is the standard format for:

# API communication
# Configuration files
# Data exchange
# Logging
# Caching


# Python Dictionary → JSON
import json

user = {
    "id": 1,
    "name": "John",
    "is_active": True
}

json_string = json.dumps(user)

print(json_string)


# JSON → Python Dictionary
data = '{"id": 1, "name": "John"}'

user = json.loads(data)

print(user["name"])


# Write JSON to File
user = {
    "name": "Alice",
    "age": 25
}

with open("user.json", "w") as file:
    json.dump(user, file)


# Pretty Printing JSON
# Useful for debugging.
with open("user.json", "w") as file:
    json.dump(user, file, indent=4)


# Read JSON File
with open("user.json") as file:
    data = json.load(file)

print(data)


# Best practices
# other best practicies listed so far apply
# Never trust external JSON. Validate required fields:

if "email" not in data:
    raise ValueError("Missing email")
