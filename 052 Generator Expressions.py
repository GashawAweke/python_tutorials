# Generator Expressions

# Produce values one at a time.

# List comprehension:


numbers = [x * 2 for x in range(1000000)]

# Creates entire list in memory.
# print(numbers)


# Generator:

numbers = (x * 2 for x in range(1000000))

# Creates values only when needed.

# Iteration
# for n in numbers:
#     print(n)


# Getting next value
numbers = (x for x in range(3))

print(next(numbers))
print(next(numbers))
