# picca_slicer.py
# Demonstrates string slices

word = "pizza"
print(
	"""
	Memo
    0   1   2   3   4   5
    +---+---+---+---+---+
    | p | i | z | z | a |
    +---+---+---+---+---+
    -5  -4  -3  -2  -1
	"""
)

print("Enter the start and end indexes for \"pizza\" slice you want to get.")
print("To exit the next loop press the key <Enter> without input start index.")
start = None
finish = None
while start != "" and finish != "":
	start = input("\nStart index: ")
	if start:
		start = int(start)
		finish = input("End index: ")
		if finish:
			finish = int(finish)
			print("Slice word[", start, ":", finish, "] seems as", end=" ")
			print(word[start:finish])

input("\n\nPress the key <Enter> to exit.")
