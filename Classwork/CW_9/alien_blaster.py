# alien_blaster.py
# Demonstrates the interaction of objects.


class Player(object):
	''' A player in action game. '''
	def blast(self, enemy):
		print("The player shots the enemy.\n")
		enemy.die()


class Alien(object):
	''' Enemy alien in action game. '''
	def die(self):
		print("Breathing heavily, the alien says: \"Well, that's all. My song is sung.\n" \
				"It\'s already getting dark before my eyes...\n" \
				"Tell one and a half million of my larvae that I loved them...\n" \
				"Farewell, ruthless world.\"")


# Main part of the program.
print("\t\tAlien death\n")

hero = Player()
invader = Alien()

hero.blast(invader)

input("\n\nPress the key <Enter> to exit.")
