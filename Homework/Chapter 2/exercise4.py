# exercise4.py -- Chapter 2
# Autodiler -- calculates total cost of a car

cost_begin = input("Enter the initial cost of your car: $")
cost_begin = int(cost_begin)

# Calculating extra charges.
tax = 0.13 * cost_begin;				# Rate is 13 % in our country.
registration = 0.02 * cost_begin 		# Registragion fee
agency = 1000							# Agency fee
delivery = 120							# Delivery cost

cost_end = cost_begin + tax + registration + agency + delivery
cost_end = int(cost_end)				# I wanted so.

print("\nThen the final cost of your car = $", end="")
print(cost_end)
input("\n\nPress the key [Enter] to exit.")
