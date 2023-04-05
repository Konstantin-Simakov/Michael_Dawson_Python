# exercise2.py
# The program prints the input text in reverse order.

text = input("Enter the text:\n")
TEXT_LEN = len(text)

print("\nIt is your text in reverse order.")
print("\n1st variant:")
for i in range(TEXT_LEN):
	print(text[-i - 1], end="")

print("\n\n2nd variant:")
for i in range(TEXT_LEN):
	print(text[(TEXT_LEN - 1) - i], end="")

print("\n\n3rd variant:")
for i in range((TEXT_LEN - 1), (0 - 1), -1):
	print(text[i], end="")

print("\n\n4th variant:")
for i in range(-1, (-TEXT_LEN - 1), -1):
	print(text[i], end="")

input("\n\nPress the key <Enter> to exit.")
