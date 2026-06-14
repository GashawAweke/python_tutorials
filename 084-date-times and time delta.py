from datetime import datetime, UTC, timedelta


# Used everywhere:

# Scheduling
# Appointments
# Logging
# Auditing
# Billing
# Reports

# now = datetime.now()
now = datetime.now(UTC)

print(now)


# avoid the old datetime.utcnow()
# Avoid for new projects.


# Access Components
print(now.year)
print(now.month)
print(now.day)


# Create Specific Date

birthday = datetime(
    year=1990,
    month=5,
    day=15
)


print(birthday)


# Format Date
now.strftime("%Y-%m-%d")
print(now)

# Common Formats
# %Y  # year
# %m  # month
# %d  # day
# %H  # hour
# %M  # minute
# %S  # second


# eg
now.strftime(
    "%Y-%m-%d %H:%M"
)


print(now)


# Parse Date String

date = datetime.strptime(
    "2026-06-13",
    "%Y-%m-%d"
)


# Date Arithmetic
today = datetime.now()

tomorrow = today + timedelta(days=1)

print(tomorrow)


# Subtract Dates
difference = tomorrow - today

print(difference.days)


# Extremely Important Production Rule

# Store timestamps in UTC.

# Good:

datetime.now(UTC)

# Bad:

datetime.now()

# Why?

# Users may be in :

# Ethiopia
# Kenya
# UAE
# UK
# USA

# Store:

# UTC

# Convert to local timezone only when displaying.

# This is how:

# Google Calendar
# Hospital systems
# Telemedicine systems
# Banking systems

# handle dates.


# Real-Life Architecture Patterns
# Audit Logs
{
    "user_id": 1,
    "action": "login",
    "timestamp": datetime.now(UTC)
}


# What You Will Use Most in Real Projects
# json.load()
# json.dump()

# datetime.now(UTC)

# timedelta()

# sqlite3.connect()

# cursor.execute()

# fetchone()
# fetchall()

# ==========
# Production-level habits:

# Always use UTC
# Always use parameterized SQL
# Always use with open()
# Always validate JSON
# Use perf_counter() for timing
# Use PostgreSQL instead of SQLite for production web apps
