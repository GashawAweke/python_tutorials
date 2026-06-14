# Inheritance allows a class to reuse and extend another class .

# Why It Matters in Cybersecurity

# Security tools often share common functionality:

# All scanners perform scans
# All alerts have timestamps
# All authentication methods verify credentials


# Syntax

# class Parent:
#     pass
# class Child(Parent):
#     pass


# Example: Security Scanner

class Scanner:
    def scan(self):
        print('performing generic scan...')


class PortScanner(Scanner):
    def scan_ports(self):
        print('scanning open ports')


scanner = PortScanner()

scanner.scan()
scanner.scan_ports()


# Real World

# Scanner
#     ├── PortScanner
#     ├── VulnerabilityScanner
#     ├── MalwareScanner
#     └── WebScanner


# Multi-level Inheritance


class Device:
    def connect(self):
        print("Device connected")


class Server(Device):
    def start(self):
        print("Server started")


class WebServer(Server):
    def host(self):
        print("Hosting web application")


web = WebServer()

web.connect()
web.start()
web.host()


# Cybersecurity Example
# Device
# ↓
# Server
# ↓
# SIEMServer

# =============
# Multiple Inheritance
# A class inherits from multiple parents.
# Example: Authentication System


class PasswordAuth:
    def verify_password(self):
        print("Password verified")


class MFAAuth:
    def verify_mfa(self):
        print("MFA verified")


class SecureLogin(PasswordAuth, MFAAuth):
    pass


login = SecureLogin()
login.verify_password()
login.verify_mfa()


# Real World
# Security systems often combine:
# Password authentication
# Biometrics
# OTP verification


# Method Resolution Order(MRO)

# Python searches parent classes in order.
# print(SecureLogin.__mro__)

# Example output:
# (SecureLogin, PasswordAuth, MFAAuth, object)


# A Good Example of Inheritance
# Designing an Intrusion Detection System(IDS)
#


class DetectionEngine:
    def detect(self):
        raise NotImplementedError


class SignatureDetection(DetectionEngine):
    def detect(self):
        print("Detecting known attack signatures")


class AnomalyDetection(DetectionEngine):
    def detect(self):
        print("Detecting unusual behavior")


# usage
engines = [
    SignatureDetection(),
    AnomalyDetection()
]

for engine in engines:
    engine.detect()
