# exercise1.py
# The program calculates when user request it.

begin = int(input("Enter a begin number: "))
end = int(input("Enter an end number: "))
step = int(input("Enter a step between every number: "))

print("Count from", begin, "to", end, 
	"not including only right border",
	"of the numerical interval in increments of", step)
for i in range(begin, end, step):
	print(i, end=" ")

input("\n\nPress the key <Enter> to exit.")
