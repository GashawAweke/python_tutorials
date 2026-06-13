# Production Rules You Should Remember

## Rule 1

One file = one responsibility.

Good:

```text
auth.py
email_service.py
payments.py
```

Bad:

```text
everything.py
```

### Rule 2

Prefer:

```python
import module
```

or

```python
from module import specific_function
```

Avoid:

```python
from module import *
```

### Rule 3

Use packages for medium and large projects.

```text
patients/
appointments/
billing/
laboratory/
```

### Rule 4

Use relative imports only inside packages.

```python
from .users import get_user
```

### Rule 5

Always protect executable code.

```python
if __name__ == "__main__":
    main()
```

This is one of the most common patterns in professional Python codebases.
