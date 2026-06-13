A package is a folder containing modules.

project/
├── auth.py
├── users.py
├── products.py
├── orders.py

Sub-packages

Packages can contain packages.

```
ecommerce/

├── users/
│ ├── customer.py
│ └── admin.py
│
└── products/
   ├── books.py
   └── electronics.py
```

Intra-package References

Modules inside a package often need each other.

```py
from .users import get_user

print(get_user())
```

The dot (.) means:
current package

```py
from ..users import get_user

```

means: go up one package level

example:

```py
from ..patients.records import get_patient

```
