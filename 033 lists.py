# example
open_ports = [22, 80, 443]

allowed_ips = [
    "192.168.1.10",
    "192.168.1.11"
]

log_files = [
    "access.log",
    "error.log",
    "auth.log"
]


# Lists use indexes.


users = ["Alice", "Bob", "Charlie"]

print(users[0])
# start counting from the end

print(users[-1])


# Slicing
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])


print(numbers[:3])
# [10, 20, 30]

print(numbers[2:])
# [30, 40, 50]

print(numbers[::-1])
# Reverse list


users[0] = 'Gashaw'
print(users)


# List Unpacking
# Extract values directly into variables.


person = ["John", 25, "Developer"]


name, age, job = person


print(name)
print(age)
print(job)


# Ignore Values

name, _, job = person
print(name)
print(job)


# Using *
# Collect remaining items.


numbers = [1, 2, 3, 4, 5]

first, *others = numbers

print(first)
# 1

print(others)
# [2, 3, 4, 5]
