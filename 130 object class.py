# Every Python class automatically inherits from object.


class Firewall:
    pass


print(issubclass(Firewall, object))  # true

# Why It Matters
# The object class provides built-in capabilities:

# __str__
# __repr__
# __eq__
# __hash__

# Everything in Python is an object.

print(isinstance(42, object))
print(isinstance("admin", object))
