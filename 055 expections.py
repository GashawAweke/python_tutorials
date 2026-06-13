# # Exceptions are Python's way of handling errors gracefully instead of crashing your program.


# # without exception handling a program crash


# try:
#     age = int(input("Age: "))
#     print(age)
# except:
#     print("Please enter a valid number")


# # Basic Exception Handling
# # Syntax
# # try:
# #     # risky code
# # except:
# #     # handle error


# try:
#     result = 10 / 0
# except:
#     print("Something went wrong")


# # Handle Specific Exceptions


# # Never catch everything blindly.

# # Bad:

# try:
#     number = int(input("Number: "))
# except:
#     print("Error")

# # Good:

# try:
#     number = int(input("Number: "))
# except ValueError:
#     print("Invalid number")


# # Common Exceptions You'll See


# # | Exception         | Cause                   |
# # | ----------------- | ----------------------- |
# # | ValueError        | Wrong value type        |
# # | TypeError         | Wrong data type         |
# # | ZeroDivisionError | Division by zero        |
# # | KeyError          | Dictionary key missing  |
# # | IndexError        | List index missing      |
# # | FileNotFoundError | File doesn't exist      |
# # | PermissionError   | No access rights        |
# # | AttributeError    | Object lacks attribute  |
# # | ImportError       | Import failed           |
# # | RuntimeError      | Generic runtime problem |


# # Different errors often require different actions.

# try:
#     age = int(input("Age: "))
#     result = 100 / age

# except ValueError:
#     print("Age must be a number")

# except ZeroDivisionError:
#     print("Age cannot be zero")


# # Multiple Exceptions Together

# try:
#     value = int(input("Value: "))
# except (ValueError, TypeError):
#     print("Invalid input")


# # Catch Exception Object


# try:
#     number = int("abc")

# except ValueError as e:
#     print(e)


# # The Else Block

# # Runs only if no exception occurred.

# try:
#     age = int(input("Age: "))

# except ValueError:
#     print("Invalid age")

# else:
#     print("Success")
#     print(age)


# # Finally Block(Cleaning Up)

# # Runs whether an exception occurs or not .

# # Very important for:

# # Database connections
# # File handles
# # Network sockets
# # API sessions


# try:
#     file = open("data.txt")

# except FileNotFoundError:
#     print("Missing file")

# finally:
#     print("Cleanup")


# # File Handling and Exceptions

# # Bad:

# file = open("report.txt")
# content = file.read()

# # File may stay open if error occurs.

# # Good:

# try:
#     file = open("report.txt")
#     content = file.read()

# finally:
#     file.close()


# # The With Statement

# # The preferred modern approach.

# # Python automatically performs cleanup.


# # Reading Files
# with open("report.txt") as file:
#     content = file.read()

# print(content)

# # File automatically closes.

# # Equivalent to:

# file = open("report.txt")

# try:
#     content = file.read()

# finally:
#     file.close()


# Why "with" Matters

# # In production systems you frequently use:

# # Files
# # Database sessions
# # Network connections
# # Locks
# # Streams


# # Multiple Resources
# with open("input.txt") as infile, \
#         open("output.txt", "w") as outfile:

#     outfile.write(infile.read())


# # Raising Exceptions

# # Sometimes you create the exception yourself.

# # Syntax:

# # raise Exception("message")


# age = -5

# if age < 0:
#     raise ValueError("Age cannot be negative")


# # Business Rule Enforcement


# def withdraw(balance, amount):
#     if amount > balance:
#         raise ValueError("Insufficient funds")

#     return balance - amount
# # This prevents invalid system states.


# # Creating Custom Exceptions
# # Useful in large applications.


# class PatientNotFoundError(Exception):
#     pass


# # Raise it:

# raise PatientNotFoundError("Patient not found")

# # Catch it:

# try:
#     raise PatientNotFoundError()

# except PatientNotFoundError:
#     print("Patient missing")


# Exception Chaining
# Preserve original error.

try:
    number = int("abc")

except ValueError as e:
    raise RuntimeError("User input invalid") from e

# Very useful for debugging large systems.


# Best Practices
# 1. Catch Specific Exceptions

# Good:

except ValueError:

    # Bad:
except:

    # 2. Never Silence Errors

    # Bad:

try:
    process()

except:
    pass
# This hides bugs.

# 3. Log Errors
try:
    process()

except Exception as e:
    logger.error(e)
# 4. Fail Fast for Invalid Data
# Good:

if age < 0:
    raise ValueError("Invalid age")

# Do not silently fix invalid data.

# ==============
# Cost of Raising Exceptions
# Exceptions are relatively expensive.
# Avoid using them for normal program flow.

# Bad:

try:
    value = users["admin"]

except KeyError:
    value = None

# Repeated millions of times can become slow.

# Better Approach
if "admin" in users:
    value = users["admin"]
# Another Example
# Bad:

try:
    number = int(user_input)
except ValueError:
    number = 0

# If invalid input is expected frequently, validate beforehand.

# =============
# Practical Production Example


def load_patient(patient_id):
    try:
        patient = database.get(patient_id)

        if patient is None:
            raise ValueError("Patient not found")

        return patient

    except DatabaseConnectionError:
        logger.error("Database unavailable")
        raise

    except ValueError:
        logger.warning("Invalid patient request")
        raise


# ==========
# The 20% You Will Use 80% of the Time
try:
    risky_operation()

except SpecificException as e:
    handle_error(e)

else:
    success_code()

finally:
    cleanup()


# ==========
# And for resources:
with open("file.txt") as file:
    content = file.read()


# ==========
# And for validation:

if invalid_data:
    raise ValueError("Invalid data")
