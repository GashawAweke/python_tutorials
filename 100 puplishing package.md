# Publishing Packages

Publishing allows others to install your package:

```bash
pip install your-package
```

## Minimal `pyproject.toml`

```toml
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "awesome-utils"
version = "0.1.0"
description = "Useful utilities"
readme = "README.md"
requires-python = ">=3.11"

authors = [
  {name = "Gashaw"}
]

dependencies = [
  "requests>=2.32"
]
```

## Build the Package

Install build tool:

```bash
pip install build
```

Build:

```bash
python -m build
```

Generated:

```text
dist/
├── awesome_utils-0.1.0.tar.gz
└── awesome_utils-0.1.0-py3-none-any.whl
```

## 12. Package Types

### Source Distribution (sdist)

```text
.tar.gz
```

Contains source code.

### Wheel

```text
.whl
```

Pre-built package for installation.

Wheels install faster and are preferred.

## 13. Test Locally

Install your package:

```bash
pip install dist/*.whl
```

Test import:

```python
import awesome_utils
```

## Upload to TestPyPI First

Create account:

- TestPyPI
- PyPI

Upload:

```bash
twine upload --repository testpypi dist/*
```

Install:

```bash
pip install \
    --index-url https://test.pypi.org/simple/ \
    awesome-utils
```

Always test before publishing to production PyPI.

## Publish to PyPI

Upload:

```bash
twine upload dist/*
```

Users can install:

```bash
pip install awesome-utils
```

## Semantic Versioning

Use:

```text
MAJOR.MINOR.PATCH
```

Examples:

```text
1.0.0
1.1.0
1.1.1
2.0.0
```

Rules:

| Change          | Version |
| --------------- | ------- |
| Bug fix         | PATCH   |
| New feature     | MINOR   |
| Breaking change | MAJOR   |

Examples:

```text
1.2.3 → 1.2.4
1.2.3 → 1.3.0
1.2.3 → 2.0.0
```
