# in Operator

# Check existence.

users = ["Alice", "Bob", "Charlie"]

print("Bob" in users)
# True

print("David" in users)
# False

# Very common in authentication and authorization systems:

allowed_roles = [
    "admin",
    "doctor",
    "teacher"
]

if "doctor" in allowed_roles:
    print("Access granted")


# index()
# Find position.

users = ["Alice", "Bob", "Charlie"]
print(users.index("Bob"))  # 1


# Check before using:

if "Bob" in users:
    print(users.index("Bob"))


# count()

# Count occurrences.

numbers = [1, 2, 2, 2, 3]

print(numbers.count(2))

# Useful for log analysis.
# example

failed_logins = [
    "user1",
    "user2",
    "user1",
    "user1"
]

print(failed_logins.count("user1"))  # 3
