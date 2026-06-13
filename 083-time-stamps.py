# Current Timestamp


import time

timestamp = time.time()

print(timestamp)


# Convert Timestamp to Integer
timestamp = int(time.time())

print(timestamp)


# Measure Execution Time

# Very common in production.


start = time.time()

for i in range(1_000_000):
    pass

end = time.time()

print(end - start)


# Better Modern Alternative

# Use:

time.perf_counter()

# instead of:

time.time()

# for benchmarking.
start = time.perf_counter()

# code

end = time.perf_counter()
print(end - start)
# Higher precision.
