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

### 3. Always Specify UTF-8

```python
open(
    "file.txt",
    encoding="utf-8"
)
```

Avoids cross-platform bugs.

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

### 5. Use Recursive Searches Carefully

```python
Path("uploads").rglob("*.pdf")
```

On huge directories this can be expensive.

Always consider the size of the filesystem.

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
