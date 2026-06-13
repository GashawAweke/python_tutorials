# Basic Loop


users = ["Alice", "Bob", "Charlie"]

for user in users:
    print(user)


# Using enumerate()
# syntax: enumerate(iterable, start=0)
# Get both index and value.


users = ["Alice", "Bob", "Charlie"]


for index, user in enumerate(users):
    print(index, user)


# real world examples
tasks = [
    "Backup database",
    "Scan logs",
    "Generate report"
]


for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")
