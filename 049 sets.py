# Sets

# A set stores unique values.

# Extremely common.


emails = [
    "john@gmail.com",
    "john@gmail.com",
    "alice@gmail.com"
]

unique_emails = set(emails)

print(unique_emails)


# Membership testing

# Very fast.


blocked_ips = {
    "192.168.1.1",
    "192.168.1.2"
}

if "192.168.1.1" in blocked_ips:
    print("Blocked")

# Cybersecurity tools use this constantly.


# Set Operations
# Union
# Combine all values.

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)

# Intersection
# Common items.
a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)  # {3}

# Difference

a = {1, 2, 3}
b = {3, 4, 5}

print(a - b)


# Real-world examples

# Finding users in both systems:

# active_users & paying_users

# Finding suspicious IPs:

# incoming_ips & blacklist_ips
