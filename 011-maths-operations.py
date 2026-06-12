# arithmetic
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 3)


# Floor Division(//)
# Returns an integer result.

# Useful when calculating:

# Number of network blocks
# Number of pages
# Chunk sizes


print(10 // 3)


# Modulus ( % )

# Returns the remainder.


print(10 % 3)


# Useful for:

# Even/odd checks
# Cyclic tasks
# Scheduling

# Cybersecurity example:
packet_count = 105

if packet_count % 5 == 0:
    print("Checkpoint reached")


# Exponent(**)

# Common in:

# Cryptography
# Binary calculations
# Networking

print(10 ** 3)  # 1000
print(2 ** 16)  # 65536


# Augmented Assignment Operators

# Shorter ways to update variables.


x = 10

x += 3
x -= 2
x *= 5
x /= 2
x //= 2
x %= 3
x **= 2

print(x)  # 13
