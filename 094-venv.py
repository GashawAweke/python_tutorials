# Why Virtual Environments?
# Without virtual environments:

# Project A → Django 4
# Project B → Django 5

# Conflict occurs because both install globally.
# Virtual environments isolate dependencies.


# Create Virtual Environment

# Modern Python:
# python -m venv .venv

# Convention:
# project/
#     .venv/
#     src/
#     app.py

# The .venv name is now the most common industry standard.


# Activate Virtual Environment

# Linux / macOS
# source .venv/bin/activate

# Windows CMD
# .venv\Scripts\activate.bat

# Windows PowerShell
# .venv\Scripts\Activate.ps1


# Deactivate Environment
# deactivate


# Verify Environment
# which python

# Linux:
# which pip

# Windows:
# where python

# You should see:
# project/.venv/bin/python


# Best Practice

# Always create a virtual environment before installing packages:

# python - m venv .venv
# source .venv/bin/activate
# python - m pip install package
