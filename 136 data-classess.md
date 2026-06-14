# Best Practices for Cybersecurity Software

### Prefer Composition over Deep Inheritance

Avoid:

```text
Device
   ↓
NetworkDevice
   ↓
Server
   ↓
LinuxServer
   ↓
WebServer
   ↓
ApacheServer
```

Prefer:

```python
class Logger:
    pass


class AlertSystem:
    pass


class IDS:
    def __init__(self):
        self.logger = Logger()
        self.alert = AlertSystem()
```

### Use ABCs for Plugin Architectures

Example:

```python
class Scanner(ABC):

    @abstractmethod
    def scan(self):
        pass
```

All plugins must implement:

```python
scan()
```

### Use Data Classes for Data Models

Good candidates:

- Security events
- Alerts
- IOC records
- Vulnerabilities
- Log entries

Modern Python security frameworks generally favor composition + abstract interfaces over deep inheritance trees because they are easier to maintain, test, and extend.
