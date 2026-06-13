# List Comprehensions
# The Pythonic way to create lists.


# Basic Syntax
# [expression for item in iterable]


squares = [x**2 for x in range(5)]

print(squares)


# With Condition


events = [x for x in range(20)
          if x % 2 == 0
          ]

print(events)


# Practical Example: File Extensions
files = [
    "report.pdf",
    "image.png",
    "notes.txt"
]

pdf_files = [file for file in files if file.endswith(".pdf")]

print(pdf_files)


# Data Cleaning
raw_data = ["10", "20", "30"]

numbers = [int(x) for x in raw_data]

print(numbers)


# Nested Comprehension

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]


flattened = [
    num
    for row in matrix
    for num in row
]


print(flattened)


# map() vs List Comprehension

# Map:
map(lambda x: x * 2, numbers)


# List Comprehension:

[x * 2 for x in numbers]

# In modern Python, list comprehensions are usually preferred because they are easier to read.


# filter() vs List Comprehension

# Filter:

filter(lambda x: x > 10, numbers)

# List Comprehension:

[x for x in numbers if x > 10]

# Again, list comprehensions are often more Pythonic.
