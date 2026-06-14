# Virtual Environments in VS Code

## Recommended Project Structure

```text
my_project/
│
├── .venv/
├── src/
│   └── main.py
├── tests/
├── Pipfile
├── requirements.txt
└── README.md
```

## Configure VS Code

Open project:

```bash
code .
```

Select interpreter:

```text
Ctrl+Shift+P
Python: Select Interpreter
```

Choose:

```text
.venv/bin/python
```

or Windows:

```text
.venv\Scripts\python.exe
```

## Verify Interpreter

Create:

```python
import sys

print(sys.executable)
```

Expected:

```text
/path/to/project/.venv/bin/python
```

# Modern Best Practices (2026)

## For Simple Projects

Use:

```bash
python -m venv .venv
pip install -r requirements.txt
```

---

## For Professional Applications

Use:

```bash
Pipenv
```

or increasingly:

```text
uv
poetry
```

The Python ecosystem is rapidly moving toward newer tools such as:

- [uv Documentation](https://docs.astral.sh/uv/?utm_source=chatgpt.com)
- [Poetry Documentation](https://python-poetry.org/?utm_source=chatgpt.com)

Many teams in 2026 prefer `uv` because it is significantly faster while supporting virtual environments and dependency management.

---

# Production Workflow Example

```bash
mkdir my_api
cd my_api

python -m venv .venv
source .venv/bin/activate

python -m pip install fastapi uvicorn

pip freeze > requirements.txt
```

Run:

```bash
uvicorn main:app --reload
```

Deploy:

```bash
pip install -r requirements.txt
```

---

# Common Commands Summary

| Task                   | Command                           |
| ---------------------- | --------------------------------- |
| Create venv            | `python -m venv .venv`            |
| Activate venv          | `source .venv/bin/activate`       |
| Install package        | `pip install package`             |
| Upgrade package        | `pip install --upgrade package`   |
| Remove package         | `pip uninstall package`           |
| Export dependencies    | `pip freeze > requirements.txt`   |
| Install dependencies   | `pip install -r requirements.txt` |
| Install Pipenv         | `pip install pipenv`              |
| Enter Pipenv shell     | `pipenv shell`                    |
| Run command            | `pipenv run python app.py`        |
| Install dev dependency | `pipenv install pytest --dev`     |

# Real-World Advice for Production

For modern backend projects such as FastAPI, AI systems, and microservices:

- Use `.venv` for small projects.
- Use dependency locking (`Pipfile.lock` or lock files).
- Commit lock files to Git.
- Never install packages globally.
- Pin versions for production systems.
- Separate development dependencies from production dependencies.
- Verify the active Python interpreter before debugging package issues.

This practice prevents the famous Python error:

```text
ModuleNotFoundError: No module named 'package'
```

which is almost always caused by installing packages into the wrong environment.
