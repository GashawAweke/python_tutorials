# Chat Application

while True:
    message = input("You: ")

    if message == "exit":
        break


# Web Server
while True:
    request = wait_for_request()
    process_request(request)
# Servers often run continuously until stopped.


# Exercise: Count Even Numbers
count = 0

for number in range(1, 10):

    if number % 2 == 0:
        print(number)
        count += 1

print(f"We have {count} even numbers")
