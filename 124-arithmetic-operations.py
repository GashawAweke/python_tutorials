# Objects can support mathematical operations.


# | Method        | Operator |
# | ------------- | -------- |
# | `__add__`     | `+`      |
# | `__sub__`     | `-`      |
# | `__mul__`     | `*`      |
# | `__truediv__` | `/`      |


# Example: Aggregating Network Traffic


class Traffic:
    def __init__(self, bytes_transferred):
        self.bytes = bytes_transferred

    def __add__(self, other):
        return Traffic(self.bytes + other.bytes)

    def __str__(self):
        return f"{self.bytes} bytes"


server1 = Traffic(5000)
server2 = Traffic(8000)

total = server1 + server2

print(total)


# Real-World Cybersecurity Use Cases
#     Summing network traffic
#     Combining IDS events
#     Aggregating log sizes
#     Calculating attack statistics
