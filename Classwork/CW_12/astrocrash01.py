# astrocrash01.py
# Only asteroids move across the screen.

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
	
	games.screen.mainloop()

# Go!
if "__main__" == __name__:
	main()
