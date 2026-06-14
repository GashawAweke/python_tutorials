# Pydoc

`pydoc` generates documentation automatically from docstrings.

## View Documentation

For built-in modules:

```bash
python -m pydoc pathlib
```

Example:

```bash
python -m pydoc json
```

## View Documentation for Your Module

```bash
python -m pydoc my_package.main
```

## Launch Documentation Server

```bash
python -m pydoc -b
```

This starts a local documentation server and opens a browser.

Very useful when exploring unfamiliar libraries.

## Access Help in Python

```python
help(str)
help(Path)
help(print)
```

Example:

```python
from pathlib import Path

help(Path.mkdir)
```

Professional Python developers use `help()` frequently.
