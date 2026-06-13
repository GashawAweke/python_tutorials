# Practical For Loop Examples

# retry logic
for attempt in range(1, 4):
    print(f"Sending email... Attempt {attempt}")

#  progress indicator

for step in range(1, 6):
    print("." * step)
# processing files
files = ["report.pdf", "data.csv", "image.png"]

for file in files:
    print("Processing:", file)
