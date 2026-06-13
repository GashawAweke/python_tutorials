# SQLite is :

# Lightweight
# Serverless
# Built into Python

# Perfect for:

# Prototypes
# Local apps
# Desktop software
# Caching
# Offline systems
import sqlite3

# Create Database
conn = sqlite3.connect("app.db")


# Create Cursor
# Cursor executes SQL commands.
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")


# Save Changes
# conn.commit()
# without commit data is not persisted


# Insert Data


cursor.execute(
    "INSERT INTO users(name, age) VALUES (?, ?)",
    ("John", 30)
)

conn.commit()


# Extremely Important Security Practice

# Never do:

# cursor.execute(
#     f"INSERT INTO users VALUES ('{name}')"
# )

# SQL Injection risk.

# Use parameters:
# cursor.execute(
#     "INSERT INTO users(name) VALUES (?)",
#     (name,)
# )

# Always.


# Query Data
cursor.execute(
    "SELECT * FROM users"
)

rows = cursor.fetchall()

print(rows)


# Loop Through Results
for row in rows:
    print(row)


# Query Single Row

cursor.execute(
    "SELECT * FROM users WHERE id = ?",
    (1,)
)

user = cursor.fetchone()

print(user)


# Close Connection
conn.close()

# Real-Life Pattern: Context Manager

# Modern approach:


with sqlite3.connect("app.db") as conn:
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users"
    )

    users = cursor.fetchall()
#


# SQLite vs PostgreSQL

# SQLite:

# Single file
# No server
# Small projects
# Desktop apps
# Testing

# PostgreSQL:

# Multi-user
# Production
# High traffic
# Concurrent access
# Enterprise systems
