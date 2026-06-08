
#  cybersecurity example
filename = "malware.exe"
# syntax: string[start:end], the end positions is not included

# [:3] – Grabs the first 3 characters.
print(filename[0:3])

# or
print(filename[:3])

# Grabs everything after the first 3 characters.
print(filename[3:])

# [:-3] – Grabs everything except the last 3 characters.
print(filename[:-3])

# [:-3] – Grabs the last 3 characters.
print(filename[-3:])


# Copy a String
# slice beginning  to end
copy_filename = filename[:]

print(copy_filename)


# Practical Cybersecurity Slicing Examples

# SPLIT => Extract

ip = "192.168.10.50"

octets = ip.split(".")

print(octets)
