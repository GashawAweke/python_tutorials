from string import Template

# Templates allow dynamic text generation.


# Basic Template
template = Template("Hello $name!")

message = template.substitute(name="Gashaw")

print(message)


# Multiple Variables

template = Template("""
Dear $name,

Your appointment is on $date.

Regards,
Hospital
""")

text = template.substitute(
    name="Abebe",
    date="June 20"
)

print(text)


# Safe Substitute

# Prevents crashes:

template.safe_substitute(name="John")

# Missing variables remain unchanged.
