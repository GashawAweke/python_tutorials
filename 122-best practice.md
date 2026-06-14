## Best Practices for Production Cybersecurity Systems

### 1. Keep State in Instance Attributes

Good:

```python
self.ip_address
self.session_token
```

Avoid storing per-user data in class attributes.

Bad:

```python
class Session:
    token = None  # shared accidentally
```

### 2. Use Factory Methods

```python
Packet.from_bytes(raw_packet)
User.from_json(data)
Alert.from_log(log_line)
```

This pattern is heavily used in security tooling.

### 3. Implement `__repr__`

Debugging security incidents becomes much easier.

```python
print(alert)
print(packet)
print(session)
```

### 4. Prefer Dataclasses for Data Models

Examples:

- IOC (Indicators of Compromise)
- CVE records
- Log entries
- Threat intelligence feeds
