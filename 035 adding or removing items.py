# append()
# Add one item at the end.

users = ["Alice", "Bob"]

users.append("Gashaw")
print(users)


# insert()

# Add at a specific position.

users = ["Alice", "Charlie"]

users.insert(1, "Bob")

print(users)


# extend()
# Add multiple items.


users = ["Alice", "Bob"]

users.extend(["Charlie", "David"])

print(users)  # ['Alice', 'Bob', 'Charlie', 'David']


# remove()

# Remove by value.


users = ["Alice", "Bob", "Charlie"]

users.remove("Bob")

# Raises an error if the item doesn't exist.
# users.remove("Bb")

print(users)


# pop()
# Remove by index.
# Last item by default

users = ["Alice", "Bob", "Charlie"]

removed = users.pop(1)

print(removed)
# Bob

print(users)
# ['Alice', 'Charlie']


# del

# Delete item or entire list.

users = ["Alice", "Bob", "Charlie"]

del users[1]

print(users)


# clear()

# Remove everything.

users.clear()

print(users)
