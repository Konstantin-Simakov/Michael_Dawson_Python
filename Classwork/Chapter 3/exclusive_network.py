# exclusive_network.py
# Demonstrates complex conditions and logical operations.

print("\tExclusive computer network")
print("\tOnly for registered users!\n")

security = 0
username = ""
while not username:
	username = input("Username: ")
password = ""
while not password:
	password = input("Password: ")

if "Konstantin" == username and "secret" == password:
	print("Hello, Konstantin!")
	security = 5
elif "Timur" == username and "pass" == password:
	print("Hello, Timur!")
	security = 3
elif "Miyamoto" == username and "hand" == password:
	print("Hello, Miyamoto!")
	security = 3
elif "Wright" == username and "feet" == password:
	print("Hello, Wright!")
	security = 3
elif "guest" == username or "guest" == password:
	print("Hello, dear guest!")
	security = 1
else:
	print("Couldn\'t enter to the system.", end=" ")
	print("It seems you are not exclusive user of this network.\n")

input("\n\nPress the key <Enter> to exit.")
