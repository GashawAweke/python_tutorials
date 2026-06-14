# a class = a blueprint and an object
#
# =========
#  Creating Classes
# Basic Syntax
# class ClassName:
#     pass


# example

class IPMonitor:
    def block_ip(self, ip):
        print(f'Blocking Ip: {ip}')


monitor = IPMonitor()
monitor.block_ip('192.169.1.18')


# ===================
# Constructors(__init__)
# A constructor initializes an object when it is created.

# Syntax
# def __init__(self, ...):
#     ...

# self refers to the current object.


class LoginAttempt:
    def __init__(self, username, ip_address):
        self.username = username
        self.ip_address = ip_address
        self.failed_attempt = 0


attempt = LoginAttempt(
    username='admin',
    ip_address='10.0.0.5'
)


print(attempt.username)
print(attempt.failed_attempt)
print(attempt.ip_address)


# Class attributes are shared by all objects. and Instance attributes belong to each object individually.


class PasswordPolicy:
    min_length = 12

    def __init__(self, username):
        self.username = username


u1 = PasswordPolicy("alice")
u2 = PasswordPolicy("bob")

print(u1.min_length)
print(u2.min_length)


# Changing Class Attribute

PasswordPolicy.min_length = 16

print(u1.min_length)
print(u2.min_length)

# =========
# Class Methods
# Class methods operate on the class itself.
# They use:

# @classmethod
# and receive:

# cls

# instead of self.


# example


class Firewall:
    blocked_count = 0

    @classmethod
    def increment_blocked(cls):
        cls.blocked_count += 1


Firewall.increment_blocked()
Firewall.increment_blocked()
Firewall.increment_blocked()
Firewall.increment_blocked()

print(Firewall.blocked_count)


# Instance methods operate on a specific object.


class SecurityAlert:
    def __init__(self, severity):
        self.severity = severity

    def send_alert(self):
        print(
            f"Sending {self.severity} alert"
        )


alert = SecurityAlert("HIGH")
alert.send_alert()


# Class Methods vs Instance Methods

# | Feature              | Instance Method | Class Method |
# | -------------------- | --------------- | ------------ |
# | First argument       | `self`          | `cls`        |
# | Access instance data | Yes             | No           |
# | Access class data    | Yes             | Yes          |
# | Called on            | Object          | Class        |


# Factory Methods(Very Common)
# Class methods are often used as factory methods.


# Example: Parse Log Entries


class SecurityLog:
    def __init__(self, ip, event):
        self.ip = ip
        self.event = event

    @classmethod
    def from_string(cls, log):
        ip, event = log.split(",")

        return cls(ip, event)


entry = SecurityLog.from_string(
    "192.168.1.5,FAILED_LOGIN"
)

print(entry.ip)
print(entry.event)


# Pro-Tip for Fast Scanning

#     If it starts with def, it is always a method.
#     If it is a variable assigned with an equals sign (=), it is an attribute.
#         If it has self. in front of it, it belongs to the instance.
#         If it sits directly under the class line with no self., it belongs to the class.
