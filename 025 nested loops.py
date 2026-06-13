# Syntax

for x in range(3):
    for y in range(2):
        print(x, y)


# Coordinates


for x in range(5):
    for y in range(3):
        print(x, y)


# Multiplication Table
for row in range(1, 6):
    for col in range(1, 6):
        print(row * col, end="\t")

    print()


# Password Brute Force Demonstration
# Useful in cybersecurity for understanding search spaces.
letters = "abc"

for first in letters:
    for second in letters:
        print(first + second)
