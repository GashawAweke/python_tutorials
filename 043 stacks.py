# A Stack follows:

# Last In First Out (LIFO):  Last In, First Out (LIFO) is a method used for inventory valuation and data management where the most recently added items are the first ones to be removed or sold


# Creating a Stack

# Python lists work perfectly.


stack = []
stack.append('A')
stack.append('B')
stack.append('C')

print(stack)


# Pop

# Remove top item:


item = stack.pop()
itemI = stack.pop(1)
print(item)
print(itemI)


# Peek

# View top item without removing:


print(stack[-1])


# Check Empty
if not stack:
    print("Empty")


# Function Call Stack

# Python itself uses a stack internally when calling functions.
