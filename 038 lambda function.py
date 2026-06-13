# A lambda function is a small anonymous function written in a single line.

# Syntax
# lambda parameters: expression

def square(x): return x * x


print(square(5))

# linter chnage to def statement enforcing PEP 8 Rule E731, which states you should never assign a lambda expression directly to a variable name if a def statement can do the exact same thing. coz It Defeats the Purpose of Lambdas

# square = lambda x: x * x

# print(square(5))


# Sorting with Lambda

# Very common in real-world applications.

users = [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 22},
    {"name": "Bob", "age": 40}
]

# In Python, the expression user["age"] is a dictionary lookup.Technically, it is called a subscript expression or bracket notation accessor.
users.sort(key=lambda user: user["age"])

print(users)
