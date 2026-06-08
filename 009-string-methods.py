text = "PYthon programming"

print(text.upper())
print(text.lower())


# Title Case

print(text.title())


# Remove Whitespace
# strip(): Removes characters from both the left and right ends of a string.
# rstrip(): Removes characters from the right end only.

# strip()
user_input = "   admin   "

print(user_input.strip())


# rstrip()
text = "admin   "

print(text.rstrip())


# Find Text

# find()
# Returns index or -1.


url = "https://example.com"

print(url.find("example"))
print(url.find("exa"))
print(url.find("le"))


#  Replace Text

log = "Failed login from 10.0.0.5"

print(log.replace("Failed", "Blocked"))


# Check Existence
url = "https://malicious-site.com"

print("malicious" in url)  # returns True

print("google" not in url)


# Starts With


url = "https://example.com"

print(url.startswith("https://"))


# Ends With


file = "payload.exe"

print(file.endswith(".exe"))


# Split Strings

log = "192.168.1.10,admin,success"

parts = log.split(",")

print(parts)


# Join Strings

octets = ["192", "168", "1", "10"]

ip = ".".join(octets)

print(ip)


# Count Occurrences
log = "failed failed success failed"

print(log.count("failed"))


# Check Character Types


port = "443"

print(port.isdigit())


# Alphabetic

print("admin".isalpha())


# Alphanumeric

print("admin123".isalnum())


# Common Cybersecurity String Operations


# suspicious file check


filename = "invoice.exe"

if filename.endswith(".exe"):
    print("Executable file detected")


#  detect malicious domain
filename = "invoice.exe"

if filename.endswith(".exe"):
    print("Executable file detected")


# parse web request


request = "GET /admin HTTP/1.1"

method, path, version = request.split()

print(method)
print(path)
print(version)
