# Zip Function

# Combines multiple iterables.

# Practical Example

# Combining:

# Patient names + IDs
# Product names + prices
# Employee names + salaries
# Student names + grades

# Syntax
# zip(iterable1, iterable2)


names = ["John", "Alice", "Bob"]
scores = [80, 90, 85]

combined = zip(names, scores)

print(list(combined))


# Looping with Zip

for name, score in zip(names, scores):
    print(name, score)


# Creating Dictionary


student_dict = dict(
    zip(names, scores)
    # zip(scores, names)
)


print(student_dict)
