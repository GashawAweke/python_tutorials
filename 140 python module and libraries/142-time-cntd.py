import time

# ===================

# `time.localtime()`
# Converts timestamp into readable date components.


now = time.localtime()

print(now.tm_zone)
print(now.tm_hour)
print(now.tm_min)


# Useful for logs:
# strftime (short for string format time) is a built-in method in Python that converts a time or date object into a readable string. It directly utilizes local time.
# While you can access individual attributes like tm_hour from time.localtime(), strftime allows you to format the entire time sequence into a single string in one go.

print(time.strftime("%H:%M:%S"))
