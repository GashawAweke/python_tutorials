
# KEYWORD ARGUMENTS

# positional arguments
def increment(number, by):
    return number + by


print(increment(2, 1))


# Keyword Arguments
print(increment(2, by=1))


# Multiple keywoard arguments


def create_user(name, age, city):
    print(name, age, city)


create_user(
    name="John",
    age=25,
    city="London"
)


# Mixing Positional and Keyword Arguments

# Allowed:

create_user(
    "John",
    age=25,
    city="London"
)

# Not allowed:

create_user(
    name="John",
    25,
    city="London"
)
