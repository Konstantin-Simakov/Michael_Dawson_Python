# counter.py
# Demonstrates using the range() function

print("Let's count:")
for i in range(10):			# == range(0, 10, 1)
	print(i, end=" ")

print("\n\nLet's list the multiples of five:")
for i in range(0, 50, 5):
	print(i, end=" ")

print("\n\nLet's count in reverse order:")
for i in range(10, 0, -1):
	print(i, end=" ")
print("\n")

# For example:
for _ in range(5):
	print("Hello!")
	

input("\n\nPress the key <Enter> to exit.")

# 1. [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 2. [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
# 3. [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
