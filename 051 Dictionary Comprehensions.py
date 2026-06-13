# Create dictionaries in one line.

# Normal:

squares = {}

for x in range(5):
    squares[x] = x * x

# Comprehension:

squares = {
    x: x * x
    for x in range(5)
}


# Filtering
squares = {
    x: x * x
    for x in range(10)
    if x % 2 == 0
}


# Convert users list to lookup table.


users = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Alice"}
]

lookup = {
    user["id"]: user
    for user in users
}


print(lookup[2])
