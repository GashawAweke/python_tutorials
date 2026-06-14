# Extending Built-in Types

# You can create custom versions of Python built-ins.

# Example: Secure List


class IPBlacklist(list):

    def add_ip(self, ip):
        if ip not in self:
            self.append(ip)


# Usage:

blacklist = IPBlacklist()

blacklist.add_ip("192.168.1.10")
blacklist.add_ip("192.168.1.10")

print(blacklist)


# example: Secure Dictionary
class AuditLog(dict):

    def log(self, event):
        self[len(self)] = event


logs = AuditLog()

logs.log("Failed login")
logs.log("Privilege escalation")

print(logs)
