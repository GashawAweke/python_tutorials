# Managing Dependencies

Dependency management is one of the most important aspects of software engineering.

## Installing Dependencies

Install package:

```bash
pip install fastapi
```

Install multiple:

```bash
pip install fastapi uvicorn sqlalchemy
```

## Freeze Dependencies

Generate requirements:

```bash
pip freeze > requirements.txt
```

Install later:

```bash
pip install -r requirements.txt
```

Example:

```text
fastapi==0.118.0
uvicorn==0.37.0
sqlalchemy==2.0.43
```

## Problem with `pip freeze`

`pip freeze` exports EVERYTHING:

- direct dependencies
- transitive dependencies

Example:

You install:

```bash
pip install requests
```

But `pip freeze` outputs:

```text
requests==2.32.0
urllib3==2.2.0
certifi==2025.0.0
charset-normalizer==3.4.0
idna==3.7
```

This can create bloated requirements.

## `pyproject.toml`

- modern dependency manager.
- Modern Python projects use:

```text
pyproject.toml
```

Example:

```toml
[project]
name = "my_package"
version = "0.1.0"
dependencies = [
    "fastapi>=0.118",
    "sqlalchemy>=2.0",
]
```

Install current package:

```bash
pip install -e .
```

Editable install:

```bash
pip install -e .
```

Changes become immediately available without reinstalling.

This is extremely useful during development.

## Development Dependencies

Example:

```toml
[project.optional-dependencies]
dev = [
    "pytest",
    "ruff",
    "mypy",
]
```

Install:

```bash
pip install -e ".[dev]"
```

## Recommended Tools for Modern Projects

| Purpose               | Tool           |
| --------------------- | -------------- |
| Packaging             | setuptools     |
| Build system          | build          |
| Linting               | ruff           |
| Type checking         | mypy           |
| Testing               | pytest         |
| Dependency management | pyproject.toml |
| Publishing            | twine          |

Install:

```bash
pip install build twine
```
