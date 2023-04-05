# maitre_d.py
# Demonstrates the interpetataion of values as condition values.

print("Welcome to the Shato-de-Perecusi!")
print("It seems that all the tables are occupied tonight.\n")

money = float(input("How many dollars do you wish to tip the maitre d\'?\n$"))
if money:
	print("Excuse me, I\'ve just been informed that one table is free. "
		+ "Here please.")
else:
	print("Have a seat, please. Will have to wait.")

input("\n\nPress the key <Enter> to exit.")
