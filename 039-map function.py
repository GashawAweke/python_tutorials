# Syntax

# map(function, iterable)

numbers = [1, 2, 3, 4]


squared = map(lambda x: x**2, numbers)

# print(squared)
print(list(squared))


# Using Normal Functions


def square(x):
    return x ** 2


result = map(square, numbers)

print(list(result))


# Usernames
users = ["john", "alice", "bob"]

upper_users = map(str.upper, users)

print(list(upper_users))


# Log Processing


log_sizes = ["1024", "2048", "512"]
sizes = list(map(int, log_sizes))

print(sizes)


# Useful when:

# Reading CSV files
# Processing API data
# Processing database records
# Converting user input
