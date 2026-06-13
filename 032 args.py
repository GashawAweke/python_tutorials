

# *args(Variable Number of Arguments)

# Use * args when you don't know how many arguments users will pass.

# Example


def multiply(*numbers):
    print(numbers)


multiply(2, 3, 4, 5)


def multiply(*numbers):
    total = 1

    for number in numbers:
        total *= number

    return total


print(multiply(2, 3, 4, 5))


# Iterating Over * args

def show_numbers(*numbers):
    for number in numbers:
        print(number)


show_numbers(1, 2, 3, 4)


# Indentation and Return Pitfall

# Incorrect:


def multiply(*numbers):
    total = 1

    for number in numbers:
        total *= number
        return total


# Output:

# 2

# The function exits after the first iteration.

# Correct:


def multiply(*numbers):
    total = 1

    for number in numbers:
        total *= number

    return total


# Output:

# 120
