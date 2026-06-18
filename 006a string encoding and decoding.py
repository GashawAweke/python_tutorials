# `encode()` Cheat Sheet

# Purpose:

# ```python
# str -> bytes
# ```

# Converts a Python string into bytes, usually before sending data over:

# * Serial ports(Arduino, ESP32)
# * Network sockets
# * Files
# * APIs

# ---

# # Syntax

# ```python
# text.encode()
# ```

# or

# ```python
# text.encode("utf-8")
# ```


# ---

# Example

message = "HELLO"

data = message.encode()

print(data)  # b'HELLO'


# Why use UTF-8?
# UTF-8 supports all Unicode characters:
# ```python
# "ሰላም".encode("utf-8")
# ```


# Why Use It?
# Many hardware and communication libraries expect bytes, not strings.

# Wrong:

# ```python
# arduino.write("HELLO")
# ```

# Correct:

# ```python
# arduino.write("HELLO".encode())
# ```


# UTF-8 Example

text = "ሰላም"

data = text.encode("utf-8")

print(data)  # b'\xe1\x88\xb0\xe1\x88\x8b\xe1\x88\x9d'


# Reverse Operation

# ```python
# bytes -> str
# ```

# Use:

# ```python
# decode()
# ```

# Example:

print(b'HELLO'.decode("utf-8"))
