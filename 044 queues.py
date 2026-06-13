# A Queue follows:

# First In First Out(FIFO)

# The first item added is the first item removed.


# Using deque

# Use collections.deque.


from collections import deque
queue = deque()


# add item
queue.append("John")
queue.append("Alice")
queue.append("Bob")

print(queue)

# Check Front Item
print(queue[0])


# Remove Item
first = queue.popleft()

print(first)


# Check Empty
if not queue:
    print("Queue empty")
