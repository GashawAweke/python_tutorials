# Python provides:
import subprocess

# This is the modern replacement for:

# os.system()

# Never use os.system() in new code.
subprocess.run(["ls", "-la"])


# Capture Output
result = subprocess.run(
    ["ls"],
    capture_output=True,
    text=True
)

print(result.stdout)


# execute another program
result = subprocess.run(
    ["ls"],
    capture_output=True,
    text=True
)

print(result.stdout)


# Check for Errors
subprocess.run(
    ["ls", "/wrong/path"],
    check=True
)


# Real-world Example: Git Automation
subprocess.run(["git", "pull"], check=True)


# Deployment scripts:
subprocess.run(["docker", "compose", "up", "-d"])


# Backup systems:
subprocess.run([
    "pg_dump",
    "-U",
    "postgres",
    "ehr"
])


# Security Warning

# ❌ Dangerous:

subprocess.run(
    f"rm {user_input}",
    shell=True
)

# This can lead to command injection.

# ✅ Safe:

subprocess.run(
    ["rm", user_input]
)

# Always pass arguments as a list.


# The biggest production mistake beginners make is using:

# random instead of secrets
# os.system() instead of subprocess
# Hardcoded email credentials instead of environment variables
# sys.argv for complex CLI tools instead of argparse
