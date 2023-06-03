# birthday_wishes.py
# Demonstrates named arguments and default parameter values.


# Positional parameters
def birthday_1(name, age):
	print("Happy birthday", name, "!", 
		"Today you are", age, "years old, aren\'t you?\n")

# Parameters with default values
def birthday_2(name="comrade Ivanov", age=1):
	print("Happy birthday", name, "!", 
		"Today you are", age, "years old, aren\'t you?\n")


# Main program

birthday_1("comrade Ivanov", 1)
birthday_1(1, "comrade Ivanov")
birthday_1(name="comrade Ivanov", age=1)
birthday_1(age=1, name="comrade Ivanov")

birthday_2()
birthday_2(name="Kate")
birthday_2(age=12)
birthday_2(name="Kate", age=12)
birthday_2("Kate", 12)

input("\n\nPress the key <Enter> to exit.")
