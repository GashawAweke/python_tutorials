# | Escape Sequence | Meaning |
# | --------------- | --------------- |
# | `\"`            | Double quote    |
# | `\'`            | Single quote    |
# | `\\`            | Backslash       |
# | `\n`            | New line        |
# | `\t`            | Tab             |
# | `\r`            | Carriage return |


message = 'the user entered \"admin\"'

path = "C:\\Windows\\System32"

print(message)
print(path)


# Better Approach

# Use raw strings.

path = r"C:\Windows\System32"


# newline
report = "Scan Started\nScan Finished"

# Tabs

print('IP\tStatus')
print('192.168.1.12\tOnline')
