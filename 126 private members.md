Python uses naming conventions for private attributes.

## Single Underscore

```python
class Firewall:
    def __init__(self):
        self._rules = []
```

Meaning:

```python
"Internal use only"
```

Python does **not** enforce privacy.

## Double Underscore (Name Mangling)

```python
class APIKeyVault:
    def __init__(self, key):
        self.__api_key = key


vault = APIKeyVault("SECRET123")

# print(vault.__api_key)  # Error
```

Internally Python changes:

```python
vault._APIKeyVault__api_key
```

## Important Reality

Python privacy is based on trust and convention.

A determined programmer can still access:

```python
print(vault._APIKeyVault__api_key)
```

## Real-World Cybersecurity Use Cases

- API keys
- Encryption secrets
- Authentication tokens
- Internal system state
