# hero's_inventory.py
# Demonstrates a tuple creation

# Let's create an empty tuple
inventory = ()

# Let's consider it as a condition
if not inventory:
	print("You are unarmed.")
input("\nPress the key <Enter> to continue.")

# Now let's create a tuple with some elements
inventory = ("sword",
			 "armour",
			 "shield",
			 "healing potion")

# Let's display this tuple on the screen
print("\nTuple content:")
print(inventory)

# Let's display all the elements of the tuple sequentially
print("\nSo, you have:")
for item in inventory:
	print(item)

input("\n\nPress the key <Enter> to exit.")
