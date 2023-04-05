# three_year_old.py
# Demonstrates 'while' loop working

print("\tWelcome to the program \'Simulator of a three-year-old child\'\n")
print("A conversation with a small child is imitated.")
print("Try to stop this nigthmare.\n")
print("Enter the next sentence " 
	+ "to stop the loop: \"Because.\" (without double quotes)")

response = ""
while response != "Because.":
	response = input("Why?\n")

print("Ah, Okay.")

input("\n\nPress the key [Enter] to exit.")
