# no_vowels.py
# Demonstrates how to create new string 
# from an orignal one with for loop.

VOWELS = "aeiouy"

message = input("Enter the text: ")
new_message = ""
print()				# Prints only '\n' character
for letter in message:
	if letter.lower() not in VOWELS:
		new_message += letter
		print("Created new string:", new_message)

print("\nHere is your text without vowels:", new_message)

input("\n\nPress the key <Enter> to exit.")
