<!-- __init__() vs __init__.py -->

| Name          | Type   | Purpose                 |
| ------------- | ------ | ----------------------- |
| `__init__()`  | Method | Initialize an object    |
| `__init__.py` | File   | Define a Python package |

Historically, **init**.py was required for packages.

In modern Python (3.3+), implicit namespace packages exist, but many projects—including production systems—still use **init**.py because it:

explicitly marks packages,
avoids import issues,
allows package-level exports.

### Empty `__init__.py`

Your file:

```text
hardware/
    __init__.py
```

can be empty:

```python
# empty file
```

Its mere existence marks the directory as a package.

---

### Advanced usage

You can expose public APIs:

```python
# hardware/__init__.py

from .serial_controller import SerialController
from .rgb_controller import RGBController
```

Then users can write:

```python
from ubu_robot.hardware import SerialController
```

instead of:

```python
from ubu_robot.hardware.serial_controller import SerialController
```

This is common in well-designed libraries.

---

## What happens if you remove them?

### Remove `__init__()` method

Your class:

```python
class SerialController:
    pass
```

Then:

```python
controller = SerialController()
controller.send("HELLO")
```

fails because:

```text
arduino was never initialized
```

---

### Remove `__init__.py`

Modern Python may still work:

```python
from ubu_robot.hardware import serial_controller
```

But:

- some tooling may behave unexpectedly,
- IDEs may lose package awareness,
- packaging can become harder.

For production systems like your robotics platform, keeping `__init__.py` is good practice.

---

## Mental model

Think of them as:

```text
__init__()
    ↓
Constructor / object setup

__init__.py
    ↓
Package setup
```

In your robot:

```python
serial = SerialController()
```

triggers:

```text
Create object
    ↓
Run __init__()
    ↓
Open USB serial
    ↓
Store connection
    ↓
Wait for Arduino reset
    ↓
Ready to send commands
```

Without `__init__()`, your robot object would exist but would not be ready to communicate with the Arduino.
