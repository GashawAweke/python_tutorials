# Python Standard Library is a collection of built-in modules

# 1. pathlib


import json
from pathlib import Path

path = Path("users.csv")

print(path)

# current directory
print(Path.cwd())

#  Home Directory
print(Path.home())


# Combine Paths

path = path.home()/"Documents"/"data.csv"
print(path)

# The / operator automatically handles:

# Linux paths
# Windows paths
# Mac paths

# ===
# Check If File Exists


path = Path("report.pdf")

print(path.exists())

# Check File or Folder
print(path.is_file())

print(path.is_dir())

#  Note the capital P in the Path
test_path = Path('/home/user/python_tutorials/055 expections.py')
print(test_path.exists())
print(test_path.is_absolute())


# Get File Information
# Useful for:
# File uploads
# Image processing
# Document management systems

test_file = Path('001-app.py')
print(test_file.name)
print(test_file.stem)
print(test_file.suffix)


# Real Life Pattern


uploaded_file = Path("patient_report.pdf")
# uploaded_file = Path("patient_report.exe")

if uploaded_file.suffix != ".pdf":
    raise ValueError("Only PDF files allowed")


# ===================
# Working With Directories

# Always use:

# parents = True
# exist_ok = True
# in automation scripts to prevent crashes if file exist

Path("logs").mkdir(
    parents=True,
    exist_ok=True
)


# Create Nested Directories


Path("data/backups/2026").mkdir(
    parents=True,
    exist_ok=True
)


path = Path(".")

for item in path.iterdir():
    print(item)


# Find Specific Files

for file in Path('.').glob('*.md'):
    print(file)


# Recursive Search
# Searches every subdirectory.
for file in Path('.').rglob('*.md'):
    print(file)


# =================
# Working With Files
# One of the most common tasks.


with open("logs.txt") as file:
    content = file.read()

print(content)


# Never do: file = open("notes.txt")
#  prefere with Open...


# Read Line By Line
# Best for large files.


# what is the difference from the above, the spacing?
with open('logs.txt') as file:
    for line in file:
        print(line)


# Write File

with open("output.txt", "w") as file:
    file.write("Hello")


#  append

with open('output.txt', 'a') as file:
    file.write('\nNew Line')


# Read JSON File
# Very common.

# with open('settings.json') as file:
#     data = json.load(file)
# print(data)


settings = {
    "theme": "dark",
    "language": "en"
}

with open("settings.json", "w") as file:
    json.dump(settings, file, indent=4)
