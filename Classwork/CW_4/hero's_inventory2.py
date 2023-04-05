# hero's_inventory2.py
# Demonstrates working with tuples

# Create a tuple with some items and display it with a for loop
inventory = ("sword",
			 "armour",
			 "shield", 
			 "helaing potion")

print("\nSo, your items:")
for item in inventory:
	print("\t", item)
input("\n\nPress the key <Enter> to continue.")

# Find out the length of a tuple
print("\nYou have", len(inventory), "item(s) in your possesion.")
input("\n\nPress the key <Enter> to continue.")

# Test for membership with an in condition operation
if "helaing potion" in inventory:
	print("You will live to fight another day.")

# Dispaly one item through an index (from -4 to 3 in this case...)
index = int(input("\nEnter the index number for an item inventory: "))
print("\nAt index", index, "is", inventory[index])

# Display a slice (from -4 to 4 in this case...)
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the index number to end a slice: "))
print("inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])

input("\n\nPress the key <Enter> to continue.")

# Concatenate two tuples
chest = ("gold", "gems")
print("\nYou find a chest. It contains:")
print(chest)
print("\nYou add the contents of the chest in your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)

input("\n\nPress the key <Enter> to exit.")
