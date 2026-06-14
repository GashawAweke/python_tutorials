# Magic Methods

# Magic methods start and end with double underscores:

# __something__

# They customize object behavior.


# ========


# __str__

# Human-readable representation.

# Without it:

# print(object)

# shows:

# <__main__.Class object at 0x...>
# Example
from dataclasses import dataclass


class Vulnerability:
    def __init__(self, cve):
        self.cve = cve

    def __str__(self):
        return f"Vulnerability: {self.cve}"


v = Vulnerability("CVE-2025-1234")

print(v)

# Output:

# Vulnerability: CVE-2025-1234

# ========
# __repr__

# Developer representation.


class Packet:
    def __init__(self, source_ip):
        self.source_ip = source_ip

    def __repr__(self):
        return (
            f"Packet(source_ip='{self.source_ip}')"
        )


packet = Packet("10.0.0.1")

print(packet)

# ===========
# __len__

# Customize len().


class BlockList:
    def __init__(self):
        self.ips = []

    def add(self, ip):
        self.ips.append(ip)

    def __len__(self):
        return len(self.ips)


bl = BlockList()

bl.add("10.0.0.1")
bl.add("10.0.0.2")

print(len(bl))

# ======

# __eq__

# Customize equality comparison.


class Device:
    def __init__(self, mac):
        self.mac = mac

    def __eq__(self, other):
        return self.mac == other.mac


d1 = Device("AA:BB:CC")
d2 = Device("AA:BB:CC")

print(d1 == d2)


# __lt__

# Customize sorting.


class Alert:
    def __init__(self, severity):
        self.severity = severity

    def __lt__(self, other):
        return self.severity < other.severity


a1 = Alert(1)
a2 = Alert(5)

print(a1 < a2)


# Advanced Pattern: Use Dataclasses

# For classes that mostly store data:

# from dataclasses import dataclass

@dataclass
class ThreatIntel:
    ip: str
    risk_score: int


intel = ThreatIntel(
    ip="8.8.8.8",
    risk_score=95
)

print(intel)

# Output:

# ThreatIntel(ip='8.8.8.8', risk_score=95)

# Python automatically creates:

# __init__
# __repr__
# __eq__

# Best for:

# Security events
# Log records
# Vulnerability reports
# Threat intelligence objects
