# syntax: f"...", variables or expressions arre placed inside {}


user = 'gashaw'

print(f'Logged in user: {user}')


# multiple variables
ip = "192.168.1.10"
port = 443

print(f'Target: {ip}:{port}')


# expression
print(f'2 + 2 = {2 + 2}')

#  function calls


username = "administrator"

print(f"Length: {len(username)}")


# Cybersecurity Examples

# Log Entry

ip = "10.0.0.5"
status = "BLOCKED"

log = f"[FIREWALL] {ip} -> {status}"

print(log)


# Alert Message


user = "john"
attempts = 8

print(
    f"ALERT: User {user} exceeded "
    f"{attempts} login attempts."
)


# Formatting Numbers


cpu_usage = 78.45678

print(f"CPU Usage: {cpu_usage:.2f}%")
