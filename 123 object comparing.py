# Python objects can be compared using special(magic) methods.


# | Method   | Operator |
# | -------- | -------- |
# | `__eq__` | `==`     |
# | `__ne__` | `!=`     |
# | `__lt__` | `<`      |
# | `__gt__` | `>`      |
# | `__le__` | `<=`     |
# | `__ge__` | `>=`     |


# Example:
# Imagine your SIEM(Security Information and Event Management) system ranks alerts by severity.


class SecurityAlert:
    def __init__(self, ip, severity):
        self.ip = ip
        self.severity = severity

    def __eq__(self, other):
        return self.ip == other.ip

    def __lt__(self, other):
        return self.severity < other.severity


alert1 = SecurityAlert("192.168.1.10", 8)
alert2 = SecurityAlert("192.168.1.20", 5)
alert3 = SecurityAlert("192.168.1.10", 9)

print(alert1 == alert3)   # True (same IP)
print(alert1 > alert2)    # True (severity comparison)


# Real-World Cybersecurity Use Cases
#     SIEM alert prioritization
#     Comparing malware samples
#     Risk scoring vulnerabilities
#     Comparing authentication events
