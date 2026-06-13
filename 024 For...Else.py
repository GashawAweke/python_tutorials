# Many languages don't have this feature.

# The else block executes only if the loop finishes normally.

successful = False

for attempt in range(3):
    print("Trying...")

    if successful:
        break

else:
    print("All attempts failed")


# Search Example
users = ["john", "alice", "bob"]

target = "mike"

for user in users:
    if user == target:
        print("Found")
        break

else:
    print("User not found")
