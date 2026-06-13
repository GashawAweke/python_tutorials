# if
temperature = 35

if temperature > 30:
    print("It's warm")
    print("Drink water")

print("Done")

# else if

temperature = 15

if temperature > 30:
    print("It's warm")
else:
    print("It's cold")

    # If-Elif-Else

temperature = 25

if temperature > 30:
    print("It's warm")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")


# ternary operators
age = 22

message = "Eligible" if age >= 18 else "Not Eligible"

print(message)
