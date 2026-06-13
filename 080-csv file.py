# CSV = Comma Separated Values
# Most common data exchange format.
import csv

# write


with open(
    "users.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow(["id", "name"])
    writer.writerow([1, "John"])

# read

with open(
    "users.csv",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)


# Dictionary Reader
with open("users.csv",           encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"])


# Dictionary Writer
users = [
    {
        "id": 1,
        "name": "gashaw"
    }
]

with open(
    "users.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["id", "name"]
    )

    writer.writeheader()
    writer.writerows(users)
