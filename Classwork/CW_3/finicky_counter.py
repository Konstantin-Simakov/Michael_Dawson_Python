# finicky_counter.py
# Demonstrates how break and continue commands work.

count = 0
while True:
	count += 1
	if count > 10:		# Break the cycle if count is more than 10
		break
	if 5 == count:		# Skip number 5
		continue
	print(count)

input("\n\nPress the key <Enter> to exit.")
