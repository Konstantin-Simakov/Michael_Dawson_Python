# losing_battle_bad.py
# Demonstrates correct work of the cycle.

print("Your hero is surrounded by a huge army of trolls.")
print("All surrounding fields are strewn with stinking green corpses of enemies.")
print("The lone hero draws his sword from its scabbard, " \
	+ "preparing for the last battle of his life.\n")

health = 10
trolls = 0
damage = 3
while health > 0:
	trolls += 1
	health -= damage
	print("By swinging your sword, your hero exterminates the evil troll," \
		+ " but he himself receives damage for", damage, "points.\n")
print("Your hero fought valiantly and killed", trolls, "trolls.")
print("But alas! He fell on the battlefield.")

input("\n\nPress the key <Enter> to exit.")

