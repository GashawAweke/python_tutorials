# Mistake 1: Comparing Boolean to True

# Bad:

if high_income == True:
    print("Approved")

# Good:

if high_income:
    print("Approved")


# Mistake 2: Using = Instead of ==

# Wrong:

if age = 18:

    # Correct:

if age == 18:

    # Mistake 3: Forgetting Colon
    # Wrong:

if age >= 18
print("Eligible")

# Correct:

if age >= 18:
    print("Eligible")
