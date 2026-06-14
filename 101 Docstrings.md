# Docstrings

Docstrings document Python code.

They are essential for:

- IDE autocomplete
- Documentation generation
- Team collaboration
- API references

## Function Docstrings

```python
def add(a: int, b: int) -> int:
    """
    Add two integers.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        Sum of the integers.
    """
    return a + b
```

## Class Docstrings

```python
class User:
    """
    Represents a system user.

    Attributes:
        name: User name.
        email: Email address.
    """

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
```

## Module Docstrings

Top of file:

```python
"""
Authentication utilities.

Provides login and JWT handling.
"""
```

## Real-World Example

```python
from pathlib import Path

def save_text(path: Path, content: str) -> None:
    """
    Save text to a file.

    Args:
        path:
            Destination file path.

        content:
            Text to write.

    Raises:
        OSError:
            If writing fails.
    """
    path.write_text(content)
```

Document exceptions explicitly.

This is very important in production systems.
