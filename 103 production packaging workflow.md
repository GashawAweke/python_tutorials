# Production Packaging Workflow

A modern Python package workflow:

```bash
# Create project
python -m venv .venv
source .venv/bin/activate

# Install tools
pip install build twine pytest ruff mypy

# Development install
pip install -e ".[dev]"

# Run tests
pytest

# Build package
python -m build

# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

# Best Practices

### Always use:

- `pyproject.toml`
- `src/` layout
- virtual environments
- semantic versioning
- type hints
- docstrings
- automated tests

### Avoid:

- global package installation
- publishing untested packages
- missing docstrings
- manually copying files into `site-packages`
- relying solely on `requirements.txt` for libraries
