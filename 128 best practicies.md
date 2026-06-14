# Best Practices (Production-Grade Python)

## 1. Prefer Properties Over Getters/Setters

Avoid Java-style code:

```python
user.get_password()
user.set_password()
```

Prefer:

```python
user.password
```

with internal validation via properties.

---

## 2. Use `_single_underscore` for Internal Members

```python
self._token
```

Use `__double_underscore` only when name mangling is truly necessary.

## 3. Make Domain Objects Comparable

Security tools often compare:

- Alerts
- Vulnerabilities
- Incidents
- Threat scores

Implement:

```python
__eq__
__lt__
```

## 4. Build Container Objects

Custom containers make code expressive:

```python
if ip in blacklist:
    block_connection()
```

instead of:

```python
if ip in blacklist.ips:
    block_connection()
```

## 5. Fail Loudly

```python
if value < 0:
    raise ValueError()
```

Avoid silent corrections:

```python
# Bad
value = max(value, 0)
```

Security systems should reject invalid states rather than hide them.
