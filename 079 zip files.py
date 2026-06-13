# Used everywhere:

# Backups
# Exports
# File uploads
# Data transfers
import zipfile
from pathlib import Path


with zipfile.ZipFile('backup.zip', 'w') as zip_file:
    zip_file.write('logs.txt')


# Add Multiple Files


with zipfile.ZipFile('backup.zip', 'w') as zip_file:
    zip_file.write('logs.txt')
    zip_file.write('output.txt')


# Read ZIP Contents
with zipfile.ZipFile(
    "backup.zip"
) as zip_file:
    print(zip_file.namelist())


# Extract ZIP
with zipfile.ZipFile(
    "backup.zip"
) as zip_file:

    zip_file.extractall("restore")


# Real Life Pattern

# Nightly backup


with zipfile.ZipFile(
    "ehr_backup.zip",
    "w"
) as zip_file:

    for file in Path("data").rglob("*"):
        if file.is_file():
            zip_file.write(file)


# Security Best Practice

# Be careful when extracting ZIP files from untrusted users.
# Attackers can include files like:
# ../../../etc/passwd
# Always validate extracted paths before extraction in production systems.
