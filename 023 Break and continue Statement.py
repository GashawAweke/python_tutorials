#  break
for attempt in range(1, 4):
    print(f"Attempt {attempt}")

    success = True

    if success:
        print("Success!")
        break


# Continue Statement

# Skip the current iteration and move to the next.

# Useful when filtering unwanted data.

for number in range(1, 6):

    if number == 3:
        continue

    print(number)
