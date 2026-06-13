# Python Standard Library Cheat Sheet

## The Parts Every Real-World Developer Uses

The Python Standard Library is a collection of built-in modules that come with Python. You don't install them separately.

Think of it like a hospital:

- pathlib → navigation system (finding rooms)
- os → building operations
- files → patient records
- zipfile → archive department
- csv → spreadsheet import/export

For backend systems, automation scripts, data processing, DevOps, ETL pipelines, and AI projects, these modules are used constantly.

---

# 1. Working With Paths (pathlib)

Modern Python uses the `pathlib` module.

Avoid older string-based path manipulation whenever possible.

```python
from pathlib import Path
```

---

## Create a Path

```python
from pathlib import Path

path = Path("users.csv")

print(path)
```

Output:

```python
users.csv
```

---

## Current Directory

```python
from pathlib import Path

print(Path.cwd())
```

Example:

```python
/home/gashaw/projects
```

Useful for:

- Debugging
- Server applications
- Deployment scripts

---

## Home Directory

```python
from pathlib import Path

print(Path.home())
```

Example:

```python
/home/gashaw
```

---

## Combine Paths

Never do this:

```python
path = "/home/gashaw/" + "data.csv"
```

Use:

```python
path = Path.home() / "Documents" / "data.csv"
```

Output:

```python
/home/gashaw/Documents/data.csv
```

Best Practice:

The `/` operator automatically handles:

- Linux paths
- Windows paths
- Mac paths

---

## Check If File Exists

```python
path = Path("report.pdf")

print(path.exists())
```

Output:

```python
True
```

---

## Check File or Folder

```python
path.is_file()

path.is_dir()
```

---

## Get File Information

```python
path = Path("report.pdf")

print(path.name)
print(path.stem)
print(path.suffix)
```

Output:

```python
report.pdf
report
.pdf
```

Useful for:

- File uploads
- Image processing
- Document management systems

---

# Real Life Pattern

Imagine users upload files into your EHR:

```python
uploaded_file = Path("patient_report.pdf")

if uploaded_file.suffix != ".pdf":
    raise ValueError("Only PDF files allowed")
```

Always validate file extensions before processing.

---

# 2. Working With Directories

Directories = folders.

---

## Create Directory

```python
from pathlib import Path

Path("logs").mkdir()
```

Creates:

```text
logs/
```

---

## Create Nested Directories

```python
Path("data/backups/2026").mkdir(
    parents=True,
    exist_ok=True
)
```

Best Practice:

Always use:

```python
parents=True
exist_ok=True
```

in automation scripts.

This prevents crashes if directories already exist.

---

## List Files

```python
from pathlib import Path

path = Path(".")

for item in path.iterdir():
    print(item)
```

Output:

```python
main.py
users.csv
logs
```

---

## Find Specific Files

```python
for file in Path(".").glob("*.csv"):
    print(file)
```

Output:

```python
users.csv
sales.csv
```

---

## Recursive Search

```python
for file in Path(".").rglob("*.pdf"):
    print(file)
```

Searches every subdirectory.

Useful for:

- Medical reports
- Student submissions
- Document indexing

---

# Real Life Pattern

Find all uploaded PDFs:

```python
reports = list(
    Path("uploads").rglob("*.pdf")
)
```

Used in:

- EHR systems
- LMS platforms
- File management systems

---

# 3. Working With Files

One of the most common tasks.

---

## Read Entire File

```python
with open("notes.txt") as file:
    content = file.read()

print(content)
```

---

## Why Use with?

Never do:

```python
file = open("notes.txt")
```

Preferred:

```python
with open("notes.txt") as file:
    ...
```

The file automatically closes.

Think of it like:

```python
try:
    open resource
finally:
    close resource
```

---

## Read Line By Line

Best for large files.

```python
with open("logs.txt") as file:
    for line in file:
        print(line)
```

---

## Write File

```python
with open("output.txt", "w") as file:
    file.write("Hello")
```

---

## Append File

```python
with open("output.txt", "a") as file:
    file.write("\nNew line")
```

---

## Read JSON File

Very common.

```python
import json

with open("settings.json") as file:
    data = json.load(file)

print(data)
```

---

## Write JSON File

```python
import json

settings = {
    "theme": "dark",
    "language": "en"
}

with open("settings.json", "w") as file:
    json.dump(settings, file, indent=4)
```

---

# Best Practice

Always specify encoding when reading text files.

```python
with open(
    "notes.txt",
    encoding="utf-8"
) as file:
    content = file.read()
```

This prevents many deployment issues.

---

# Real Life Pattern

Application logs:

```python
with open(
    "app.log",
    "a",
    encoding="utf-8"
) as file:
    file.write("User logged in\n")
```

---

# 4. Working With ZIP Files

Module:

```python
import zipfile
```

Used everywhere:

- Backups
- Exports
- File uploads
- Data transfers

---

## Create ZIP

```python
import zipfile

with zipfile.ZipFile(
    "backup.zip",
    "w"
) as zip_file:
    zip_file.write("data.csv")
```

---

## Add Multiple Files

```python
with zipfile.ZipFile(
    "backup.zip",
    "w"
) as zip_file:

    zip_file.write("users.csv")
    zip_file.write("orders.csv")
```

---

## Read ZIP Contents

```python
with zipfile.ZipFile(
    "backup.zip"
) as zip_file:

    print(zip_file.namelist())
```

Output:

```python
['users.csv', 'orders.csv']
```

---

## Extract ZIP

```python
with zipfile.ZipFile(
    "backup.zip"
) as zip_file:

    zip_file.extractall("restore")
```

---

# Real Life Pattern

Nightly backup:

```python
from pathlib import Path
import zipfile

with zipfile.ZipFile(
    "ehr_backup.zip",
    "w"
) as zip_file:

    for file in Path("data").rglob("*"):
        if file.is_file():
            zip_file.write(file)
```

Common in:

- EHR systems
- LMS systems
- Database exports

---

# Security Best Practice

Be careful when extracting ZIP files from untrusted users.

Attackers can include files like:

```text
../../../etc/passwd
```

Always validate extracted paths before extraction in production systems.

---

# 5. Working With CSV Files

CSV = Comma Separated Values

Most common data exchange format.

Used by:

- Excel
- Google Sheets
- Hospitals
- Schools
- Governments

---

## Read CSV

```python
import csv

with open(
    "users.csv",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Output:

```python
['id', 'name']
['1', 'John']
```

---

## Write CSV

```python
import csv

with open(
    "users.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow(["id", "name"])
    writer.writerow([1, "John"])
```

---

## Dictionary Reader

Preferred for real applications.

CSV:

```csv
id,name,email
1,John,john@test.com
```

Code:

```python
import csv

with open(
    "users.csv",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])
```

Output:

```python
John
```

---

## Dictionary Writer

```python
import csv

users = [
    {
        "id": 1,
        "name": "John"
    }
]

with open(
    "users.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["id", "name"]
    )

    writer.writeheader()
    writer.writerows(users)
```

---

# Real Life Pattern

Importing student records:

```python
import csv

students = []

with open(
    "students.csv",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for row in reader:
        students.append(row)
```

Used in:

- School management systems
- LMS imports
- EHR patient imports

---

# Production-Level Best Practices

### 1. Prefer pathlib Over os.path

Old:

```python
import os

os.path.join(...)
```

Modern:

```python
from pathlib import Path

Path(...) / "file.txt"
```

---

### 2. Always Use Context Managers

Good:

```python
with open(...) as file:
    ...
```

Bad:

```python
file = open(...)
```

---

### 3. Always Specify UTF-8

```python
open(
    "file.txt",
    encoding="utf-8"
)
```

Avoids cross-platform bugs.

---

### 4. Use DictReader and DictWriter for CSV

Avoid:

```python
row[2]
```

Prefer:

```python
row["email"]
```

More readable and less error-prone.

---

### 5. Use Recursive Searches Carefully

```python
Path("uploads").rglob("*.pdf")
```

On huge directories this can be expensive.

Always consider the size of the filesystem.

---

### 6. Never Trust Uploaded Files

Validate:

- Extension
- MIME type
- Size
- Content

Do not trust:

```python
virus.exe.pdf
```

---

### 7. Keep File Paths Out of Business Logic

Bad:

```python
Path("/home/gashaw/project/data")
```

Better:

```python
DATA_DIR = Path("data")
```

Or load from configuration.

---

# The 20% You Will Use 80% of the Time

```python
from pathlib import Path

Path.cwd()
Path.home()
Path.exists()
Path.is_file()
Path.is_dir()
Path.mkdir()
Path.iterdir()
Path.glob()
Path.rglob()

with open(...) as file:
    file.read()

with open(..., "w") as file:
    file.write(...)

import json
json.load()
json.dump()

import csv
csv.DictReader()
csv.DictWriter()

import zipfile
zipfile.ZipFile()
```

If you master these APIs, you can already build file uploads, exports, backups, data imports, logging systems, report generators, ETL scripts, and many automation tools used in production applications.
