# endless_cycle.py
# Demonstrate endless cycle working -- bad program

counter = 0
while counter <= 10:
	print(counter)
	counter += 1

input("\n\nPress the key <Enter> to exit.")