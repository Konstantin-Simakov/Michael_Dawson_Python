# exercise5.py
# Function calculates the factorial of a number with only 'for' loop.

def factorial(num):
	''' Calculates the factorial of a num. '''
	res = None
	
	if num >= 0:
		res = 1
		for i in range(1, num+1):
			res *= i

	return res


def main():
	''' Main program '''
	num = int(input("Enter a number (<= 0 to exit): "))
	while num >= 0:
		print(num, end="! = ")
		print(factorial(num))
		
		num = int(input("Enter next number (<= 0 to exit): "))


# Program launch (global scope only).
main()
input("\n\nPress the key <Enter> to exit.")
