# handle_it.py
# Demonstrates handling exceptions.

# try/except
try:
	num = float(input("Enter a number: "))
except:
	print("Likely it\'s not a number!")

# Handling a specific type of exception.
try:
	num = float(input("\nEnter a number: "))
except ValueError:
	print("It\'s not a number!")

# Handling some different type of exceptions.
print()
for value in (None, "Hi"):
	try:
		print("I try to convert to number:", value, "-->", end=" ")
		print(float(value))
	except (TypeError, ValueError):
		print("Likely it\'s not a number!")

print()
for value in (None, "Hi!"):
	try:
		print("I try to convert to number:", value, "-->", end=" ")
		print(float(value))
	except TypeError:
		print("I can convert only to strings and numbers!")
	except ValueError:
		print("I can convert only to strings consisted of numbers.")

# Getting an argument.
try:
	num = float(input("\nEnter a number: "))
except ValueError as e:
	print("It\'s not a number! Interpreter says us like:")
	print(e)

# try/except/else
try:
	num = float(input("\nEnter a number: "))
except ValueError:
	print("It\'s not a number!")
else:
	print("You entered the number", num)

input("\n\nPress the key <Enter> to exit.")
