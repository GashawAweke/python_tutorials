
# Pipenv Documentation: https: // pipenv.pypa.io/

# Pipenv combines:

# pip
# virtual environments
# dependency locking

# Similar to:

# Node.js:
# package.json
# package-lock.json

# Python:

# Pipfile
# Pipfile.lock

# Install Pipenv
# pip install pipenv

# or:

# python - m pip install pipenv

# Create Environment Automatically
# pipenv install

# Pipenv automatically:
# 1. Creates virtual environment
# 2. Creates Pipfile
# 3. Creates Pipfile.lock

# Install Package
# pipenv install requests

# Development dependency:
# pipenv install pytest - -dev

# Equivalent to:
# npm install - D

# Activate Shell
# pipenv shell

# Run command without entering shell:
# pipenv run python app.py

# Remove Package
# pipenv uninstall requests

# Dependency Tree
# pipenv graph
# Very useful for debugging dependency conflicts.
