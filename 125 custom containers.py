# Making Custom Containers

# A class can behave like built-in containers such as lists or dictionaries.

# Useful magic methods:


# | Method         | Purpose      |
# | -------------- | ------------ |
# | `__len__`      | `len(obj)`   |
# | `__getitem__`  | `obj[index]` |
# | `__setitem__`  | assignment   |
# | `__contains__` | `in`         |
# | `__iter__`     | iteration    |


# Example: Blacklisted IP Container


class Blacklist:
    def __init__(self):
        self.ips = []

    def add(self, ip):
        self.ips.append(ip)

    def __contains__(self, ip):
        return ip in self.ips

    def __len__(self):
        return len(self.ips)

    def __iter__(self):
        return iter(self.ips)


blacklist = Blacklist()

blacklist.add("10.0.0.5")
blacklist.add("192.168.1.100")

print("10.0.0.5" in blacklist)
print(len(blacklist))

for ip in blacklist:
    print(ip)


# Real-World Cybersecurity Use Cases
#      IP blacklists
#      Threat intelligence feeds
#      Malware signature databases
#      User session collections
