import secrets
import random

number = random.randint(1, 10)
print(number)


value = random.random()  # 0.0 <= x < 1.0
print(value)


# Random Choice
colors = ["red", "green", "blue"]

color = random.choice(colors)
print(color)


# Shuffle a List
cards = ["A", "K", "Q", "J"]

random.shuffle(cards)

print(cards)


# Random Sample (Without Replacement)
students = ["A", "B", "C", "D"]
selected = random.sample(students, k=2)

print(selected)

# Important Security Rule

# Never use random for:

# Passwords
# Tokens
# OTPs
# API keys

# Use secrets instead:


token = secrets.token_urlsafe(32)
print(token)

# Real-world:

# Password reset links
# Authentication tokens
# Session IDs
