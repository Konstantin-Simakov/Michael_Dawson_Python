# granted_or_denied.py
# Suggest two alternative ways.

print("Welcome to LLC \"Security Systems\".")
print("-- Security is our second name.\n")

password = input("Enter password: ")
if "secret" == password:
	print("Access is open")
	print("Welcome! You must be a very important gentleman.")
else:
	print("Access closed.")
	print("Go away!")

input("\n\nPress the key [Enter] to exit.")
