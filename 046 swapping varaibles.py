# Swapping Variables

# Python has a clean way to swap values.


x = 10
y = 20


x, y = y, x

print(x, y)  # 20 10


# Real-world use

# Sorting algorithms

numbers = [5, 3]

numbers[0], numbers[1] = numbers[1], numbers[0]
