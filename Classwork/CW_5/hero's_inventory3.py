# hero's_inventory3.py
# Demonstrates lists

# Create a list with some items and display with a for loop
inventory = ["sword", "armour", "shield", "healing potion"]
print("Your items:")
for item in inventory:
	print(item)

input("\nPress the key <Enter> to continue.")

# Get the length of the list
print("You have", len(inventory), "items in your possession.")

input("\nPress the key <Enter> to continue.")

# Test for membership with in
if "healing potion" in inventory:
	print("You will live to fight another day.")

# Display one item through an index
index = int(input("\nEnter the index for an item in inventory: "))
print("At index", index, "is", inventory[index])

# Display a slice
start = int(input("\nEnter the index to begin a slice: "))
finish = int(input("\nEnter the index to end a slice: "))
print("inventory[", start, ":", finish, "] =", end=" ")
print(inventory[start:finish])

input("\nPress the key <Enter> to continue.")

# Concatenate two lists
chest = ["gold", "gems"]
print("\nYou find a chest with contains:")
print(chest)
print("You add the content of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)

input("\nPress the key <Enter> to continue.")

# Assign by index
print("You trade your sword for a crossbow.")
inventory[0] = "crossbow";
print("Your inventory is now:")
print(inventory)

input("\nPress the key <Enter> to continue.")

# Assing by slice
print("You use your gold and gems to buy an orb of future telling.")
inventory[4:6] = ["orb of futurer telling"]
print("Your inventory is now:")
print(inventory)

input("\nPress the key <Enter> to continue.")

# Delete an item
print("In a great battle, your shield is destroyed.")
del inventory[2]
print("Your inventory is now:")
print(inventory)

input("\nPress the key <Enter> to continue.")

# Delete a slice
print("Your crossbow and armour are stolen by thieves.")
del inventory[:2]
print("Your inventory is now:")
print(inventory)

input("\n\nPress the key <Enter> to exit.")
