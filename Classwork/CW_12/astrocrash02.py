# astrocrash02.py
# Asteroids move across the screen and
# the ship can rotates.

import random
from superwires import games

games.init(screen_width=640, screen_height=480, fps=50)

class Asteroid(games.Sprite):
	""" An asteroid moving in a straight line across the screen. """
	SMALL = 1
	MEDIUM = 2
	LARGE = 3
	images = {SMALL: games.load_image("asteroid_small.bmp"),
			  MEDIUM: games.load_image("asteroid_medium.bmp"),
			  LARGE: games.load_image("asteroid_large.bmp")}
	SPEED = 2

	def __init__(self, x, y, size):
		""" Initialize a sprite with the asteroid picture. """
		super().__init__(
				image=Asteroid.images[size],
				x=x,
				y=y,
				dx=random.choice([-1, 1]) * Asteroid.SPEED * random.random()/size,
				dy=random.choice([-1, 1]) * Asteroid.SPEED * random.random()/size)
		self.size = size

	def update(self):
		""" Make the asteroid go around the screen. """
		if self.top > games.screen.height:
			self.bottom = 0
		if self.bottom < 0:
			self.top = games.screen.height
		if self.left > games.screen.width:
			self.right = 0
		if self.right < 0:
			self.left = games.screen.width


class Ship(games.Sprite):
	""" Player's ship. """
	IMAGE = games.load_image("ship.bmp")
	ROTATION_STEP = 3

	def update(self):
		""" Rotate the ship when arrow keys is pressed. """
		if games.keyboard.is_pressed(games.K_LEFT):
			self.angle -= Ship.ROTATION_STEP
		if games.keyboard.is_pressed(games.K_RIGHT):
			self.angle += Ship.ROTATION_STEP


def main():
	# Set background.
	nebula_iamge = games.load_image("nebula.jpg")
	games.screen.background = nebula_iamge

	# Create 8 asteroids.
	for i in range(8):
		x = random.randrange(games.screen.width)
		y = random.randrange(games.screen.height)
		size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])

		new_asteroid = Asteroid(x=x, y=y, size=size)
		games.screen.add(new_asteroid)

	# Create the ship.
	the_ship = Ship(
			image=Ship.IMAGE,
			x=games.screen.width/2,
			y=games.screen.height/2)
	games.screen.add(the_ship)
	
	# Start the main event loop.
	games.screen.mainloop()

# Go!
if "__main__" == __name__:
	main()
