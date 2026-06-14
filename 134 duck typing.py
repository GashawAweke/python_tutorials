# Duck Typing

# Python cares about behavior, not type.

# "If it walks like a duck and quacks like a duck, it's a duck."

# Example


class VPN:
    def connect(self):
        print("VPN connected")


class SSHClient:
    def connect(self):
        print("SSH session established")


# Function:


def establish_connection(service):
    service.connect()


# Usage:

establish_connection(VPN())
establish_connection(SSHClient())


# Used heavily in :

# Plugins
# Frameworks
# APIs
# Adapters

# No inheritance required.
