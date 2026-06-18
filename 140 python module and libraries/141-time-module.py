# The time module provides functions for working with time, delays, and timestamps.
import time


# ===================

# `time.sleep()`

# Syntax:

# ```python
# time.sleep(seconds)
# ```

# Example:
# This pauses the Python program for 2 seconds.

print('program started')

time.sleep(2)

print('sleep for 2 second')


# Why is this necessary?

# When Python opens a serial connection to Arduino, most Arduino boards automatically reset.

# The Arduino needs time to:

# 1. reboot,
# 2. run `setup()`,
# 3. become ready for communication.

# Without the delay:

# ```python
# self.serial.send("EYES_BLUE")
# ```

# might be sent before Arduino is ready, causing lost commands.

# ---


# ===================

# `time.time()`
# Returns the current Unix timestamp.
# example measuring the duration a program takes:
start = time.time()

# do_something()
time.sleep(2)


end = time.time()

elapsed = end - start

print(elapsed)

# ===================
# `time.perf_counter()`
# High precision timer.
# Best for benchmarking.
# More accurate than `time.time()`.


start = time.perf_counter()

# do_something()
time.sleep(2)


end = time.perf_counter()

elapsed = end - start

print(elapsed)


# ===================
# `time.localtime()`
# Converts timestamp into readable date components.
