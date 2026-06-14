# pip is Python's package manager.

# Equivalent:

# | Ecosystem | Package Manager |
# | --------- | --------------- |
# | Python    | pip             |
# | Node.js   | npm             |
# | Rust      | cargo           |


# Check pip version
# pip - -version

# or

# python - m pip - -version

# Production best practice:

# python - m pip install package_name

# This guarantees the package installs into the correct Python interpreter.


# Upgrade Package
# python - m pip install - -upgrade package_name

# Upgrade pip itself
# python - m pip install - -upgrade pip

# Uninstall Package
# pip uninstall package_name

# List Installed Packages
# pip list

# Show Package Information
# pip show package_name


# Export Installed Packages
# pip freeze > requirements.txt


# Install later:
# pip install - r requirements.txt


# Real-World Workflow

# Clone a project:

# git clone my_project
# cd my_project
# pip install - r requirements.txt

# This is one of the most common workflows in professional Python development.
