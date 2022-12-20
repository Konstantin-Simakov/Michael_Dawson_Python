# quotation_manipulation.py
# Demonstrates string methods

# It's the quote from Thomas Watson, who was the director of IBM in 1943.
quote = "I think it will be possible to sell about five computers on the world market."
print("Original quote:")
print(quote)

print("\nThe same in upper case:")
print(quote.upper())
print("\nThe same in lower case:")
print(quote.lower())
print("\nAs title:")
print(quote.title())
print("\nWith a little change:")
print(quote.replace("I", "Thomas Watson"))
print("\nWith swapping case:")
print(quote.swapcase())

quote = quote.upper()
print("\nAnd that's original quote again:")
print(quote)
print("\nUsing capitalize() method:")
print(quote.capitalize())

input("\n\nPress the key [Enter] to exit.")
