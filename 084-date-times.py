from datetime import datetime, UTC


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
