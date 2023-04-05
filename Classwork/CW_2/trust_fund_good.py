# trust_fund_good.py
# Demonstrates type conversion

print(
"""
			Rentier
The program calculates your monthly expenses. You need to know these statistics 
so that you don’t run out of money and you don’t have to look for a job.
Enter the amounts of expenses for all items listed below. You are rich, 
so do not trifle, write the amounts in dollars, without cents.
"""
)

car = input("'Lamborgini' car maintenance: $")
car = int(car)

rent = int(input("Rent a luxury apartment in Manhattan: $"))
jet = int(input("Rent an aircraft: $"))
gifts = int(input("Gifts: $"))
food = int(input("Lunch and dinner in resaurants: $"))
staff = int(input("Salary of servants (butler, cook, driver, secretary): $"))
guru = int(input("Salary of personal psychoanalyst: $"))
games = int(input("Computer games: $"))

total = car + rent + jet + gifts + food + staff + guru + games
print("\nTotal: $", end="")
print(total)

input("\n\nPress the key [Enter] to exit.")
