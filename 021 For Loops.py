# A for loop is used to repeat a task by iterating over an iterable object.

# Basic Syntax
# for item in iterable:
#     print(item)


# Range()
for number in range(3):
    print(number)


for number in range(3):
    print(number)

    # User-Friendly Counting
for attempt in range(1, 4):
    print("Attempt", attempt)


# Attempt 1
# Attempt 2
# Attempt 3


# Range Parameters
# range(start, stop, step), stop not included


for number in range(1, 10, 2):
    print(number)

    # Reverse Loop
for number in range(10, 0, -1):
    print(number)
