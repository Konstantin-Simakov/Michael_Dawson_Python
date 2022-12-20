# message_analyzer.py
# Demonstrates working len() function and in operator

message = input("Enter the line: ")
print("\nThe length of your input line is:", len(message))
print("\nThe most common English letter, \'e\',")
if "e" in message:
	print("is in your line.")
else:
	print("isn\'t in your line.")

input("\n\nPress the key <Enter> to exit.")
