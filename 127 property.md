# Properties

Properties allow controlled access to attributes.

They provide:

- Validation
- Computation
- Encapsulation
- Read-only values

## Without Properties (Bad)

```python
class PasswordPolicy:
    def __init__(self):
        self.min_length = 8
```

Users can set invalid values:

```python
policy.min_length = -5
```

## With Properties (Good)

```python
class PasswordPolicy:
    def __init__(self):
        self._min_length = 8

    @property
    def min_length(self):
        return self._min_length

    @min_length.setter
    def min_length(self, value):
        if value < 8:
            raise ValueError(
                "Password length must be at least 8"
            )

        self._min_length = value


policy = PasswordPolicy()

policy.min_length = 12

print(policy.min_length)
```

Output:

```python
12
```

Invalid assignment:

```python
policy.min_length = 4
```

Output:

```python
ValueError: Password length must be at least 8
```

## Read-Only Property Example

In security systems, some values should never be modified.

```python
import hashlib

class FileHash:
    def __init__(self, content):
        self._content = content

    @property
    def sha256(self):
        return hashlib.sha256(
            self._content.encode()
        ).hexdigest()


malware = FileHash("malicious payload")

print(malware.sha256)
```

No setter exists:

```python
malware.sha256 = "fake"
```

Output:

```python
AttributeError
```

## Real-World Cybersecurity Use Cases

- Password policies
- Read-only hashes
- Risk scores
- User permissions
- Certificate information
