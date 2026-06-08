# Practical Cybersecurity Slicing Examples

# SPLIT
#  breaks a string into a list of smaller strings wherever the specified character (in this case, a dot ".") appears.

# Basic Syntax: string.split(separator, maxsplit)

ip = "192.168.10.50"

octets = ip.split(".")

print(octets)


#  extract domain
email = "admin@example.com"
domain = email.split("@")[1]
print(domain)


# INDEX

# Syntax: string.index(value, start, end)
# Returns: The index integer(starts at 0).

#  Basic Search
print("apple".index("p"))      # Returns 1

# Specific Substring
# Returns 6 (starts at 'w')
print("hello world".index("world"))


# Start & End Range
# Search for "a" starting from index 3
print("banana".index("a", 3))  # Returns 3


url = "https://example.com"

protocol = url[:url.index(":")]

print(protocol)

# Use .find() instead if you do not want your code to crash when a character is missing.
# "apple".index("z") → ❌ Crashes (ValueError)
# "apple".find("z") →  Returns - 1
