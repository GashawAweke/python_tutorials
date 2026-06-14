# Modern Project Structure

```text
my_package/
│
├── pyproject.toml
├── README.md
├── LICENSE
├── .gitignore
├── src/
│   └── my_package/
│       ├── __init__.py
│       └── main.py
│
├── tests/
│   └── test_main.py
│
└── .venv/
```

### Why `src/` layout?

Prevents accidental imports from local files and catches packaging mistakes early.

This is the preferred structure in professional Python projects.
