# Arrays

# Python's standard array is usually a list.


# Real Array Module

# Useful when all values are same type.


from array import array

numbers = array("i", [1, 2, 3, 4])

print(numbers)


# Common type codes:


# | Code | Type    |
# | ---- | ------- |
# | i    | Integer |
# | f    | Float   |
# | d    | Double  |


temperatures = array("f", [36.5, 37.2, 38.0])
