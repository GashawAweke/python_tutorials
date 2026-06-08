# Multi-line Strings

report = '''

Security Scan Report

Target: 192.168.1.10
Status: Vulnerable
Severity: High


'''

print(report)
print(type(report))

# String Length
# len()

print(len(report))

# use case example
password = 'abc123'

if len(password) < 12:
    print('weak password')


# Accessing Chars

name = 'gashaw'

print(name[0])
print(name[5])


print(name[-3])
print(name[-3:])
