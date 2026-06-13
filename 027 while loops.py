
# Syntax

# while condition:
#     do_something()


# Countdown Example
number = 100

while number > 0:
    print(number)
    number //= 2


# User Input Loop
command = ""

while command.lower() != "quit":
    command = input("> ")
    print("Echo:", command)

# Input Validation Pattern:  Very common in real-world software.
age = -1

while age < 0:
    age = int(input("Enter age: "))


# Infinite Loops

while True:
    print("Running...")


# Safe Infinite Loop
while True:

    command = input("> ")

    if command.lower() == "quit":
        break

    print("Echo:", command)
