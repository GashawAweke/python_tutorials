# Same interface, different behavior.

# Example


class Firewall:
    def inspect(self):
        print("Inspecting packets")


class Antivirus:
    def inspect(self):
        print("Scanning files")


class IDS:
    def inspect(self):
        print("Monitoring network traffic")


# Usage:

tools = [
    Firewall(),
    Antivirus(),
    IDS()
]

for tool in tools:
    tool.inspect()

# Output:
   # Inspecting packets
   # Scanning files
   # Monitoring network traffic


# Benefit: You write generic code:

def run_security_check(tool):
    tool.inspect()
