# Filter Function

# filter() selects items that satisfy a condition.

# Syntax
# filter(function, iterable)


numbers = [1, 2, 3, 4, 5, 6]


even_numbers = filter(lambda x: x % 2 == 0, numbers)


print(list(even_numbers))


# Active Users


users = [
    {"name": "John", "active": True},
    {"name": "Alice", "active": False},
    {"name": "Bob", "active": True}
]


active_users = filter(lambda user: user["active"], users)


print(list(active_users))


# Cybersecurity Example
# Filter suspicious IPs:

failed_attempts = [1, 8, 15, 2, 20]

suspicious = filter(lambda attempt: attempt > 10, failed_attempts)


print(list(suspicious))
