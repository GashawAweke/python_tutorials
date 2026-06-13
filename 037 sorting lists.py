# Sorting Lists
# sorted()

# Returns a new sorted list. Original list remains unchanged.

numbers = [5, 2, 8, 1]

result = sorted(numbers)

print(result)


# sort()

# Sorts in place.

numbers = [5, 2, 8, 1]

numbers.sort()

print(numbers)


# Reverse Sorting
numbers.sort(reverse=True)

print(numbers)

# Sorting Strings
users = ["Charlie", "Alice", "Bob"]

users.sort()

print(users)


# Sorting with key

# Sort by string length.

files = [
    "error.log",
    "app.log",
    "security.log"
]

files.sort(key=len)

print(files)


# Sorting Dictionaries

# Very common in real applications.

students = [
    {"name": "John", "score": 80},
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 70}
]


students.sort(
    key=lambda student: student["score"], reverse=True
)

print(students)
