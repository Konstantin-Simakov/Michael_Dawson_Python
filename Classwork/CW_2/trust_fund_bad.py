# trust_fund_bad.py
# Demonstrates semantic error

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
rent = input("Rent a luxury apartment in Manhattan: $")
jet = input("Rent an aircraft: $")
gifts = input("Gifts: $")
food = input("Lunch and dinner in resaurants: $")
staff = input("Salary of servants (butler, cook, driver, secretary): $")
guru = input("Salary of personal psychoanalyst: $")
games = input("Computer games: $")

total = car + rent + jet + gifts + food + staff + guru + games
print("\nTotal: $", end="")
print(total)

input("\n\nPress the key [Enter] to exit.")
