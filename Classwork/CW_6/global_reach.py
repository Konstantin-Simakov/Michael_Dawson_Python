# global_reach.py
# Demonstrates working with global variables


def read_global():
	print("In the read_global() scope global value of \'value\' equals", value)

def shadow_global():
	value = -10
	print("In the shadow_global() scope local value of \'value\' equals", value)

def change_global():
	global value
	value = -10
	print("In the change_global() scope global value of \'value\' equals", value)


# Main program

# value is a global variable because now we are in the global scope
value = 10
print("In the global scope value of \'value\' equals", value, "\n")

read_global()
print("Return to the global scope. \'value\' still equals", value, "\n")

shadow_global()
print("Return to the global scope. \'value\' still equals", value, "\n")

change_global()
print("Return to the global scope. \'value\' has changed to", value, "\n")

input("\n\nPress the key <Enter> to exit.")
