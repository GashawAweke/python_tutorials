# A module is simply a Python file.
from math_utils import *
import math_utils


# Import Specific Functions
from math_utils import add

# Import Multiple Functions
from math_utils import add, multiply

# import everything
# Avoid this in production because it pollutes the namespace.
# Bad:
# from math_utils import *
# Good:
# print(math_utils.add(10, 15))
# or
# Import Specific Functions

print(add(10, 20))

# =============
# Large systems like:

# Django
# FastAPI
# NumPy

# are composed of thousands of modules.

# ===============
# 2. Compiled Python Files
# When Python imports a module, it compiles it to bytecode.
# Example:


# Python automatically creates:

# __pycache__/
# math_utils.cpython-313.pyc

# The .pyc file contains compiled bytecode.

# Purpose:

# Faster imports
# No need to recompile every time

# You normally never touch these files.
