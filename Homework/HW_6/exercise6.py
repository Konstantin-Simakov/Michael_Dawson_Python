# exercise6.py
# Function exchanges two values of its parameters.

def swap(x, y):
	''' Value exchange function for two variables. '''
	temp = x
	x = y
	y = temp

	return x, y


def main():
	''' Main program. '''
	
	# Initial values
	x = 5
	y = 10
	print("Initial values:")
	print("x =", x, end="; ")
	print("y =", y)

	# Exchange values
	x, y = swap(x, y)
	print("\nAfter swapping:")
	print("x =", x, end="; ")
	print("y =", y)


# Program launch
main()
input("\n\nPress the key <Enter> to exit.")
