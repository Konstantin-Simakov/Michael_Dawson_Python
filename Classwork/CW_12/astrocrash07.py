# astrocrash07.py
# 
# Asteroids move across the screen and
# the ship can rotates.
# When the player turns on the ship's engine, 
# the speed changes appropriately based on the angle of the ship, 
# and a characteristic sound is heard.
# Missiles were added.
# Add Fire density control was added.
# Colision processing was added.
# Wrapper was added.
# Explosions was added.
# 

import math, random
from superwires import games

games.init(screen_width=640, screen_height=480, fps=50)

class Wrapper(games.Sprite):
	""" The sprite moves around the graphic screen. """
	def update(self):
		""" Moves the sprite to the opposite side of the window. """
		if self.top > games.screen.height:
			self.bottom = 0
		if self.bottom < 0:
			self.top = games.screen.height
		if self.left > games.screen.width:
			self.right = 0
		if self.right < 0:
			self.left = games.screen.width

	def die(self):
		""" Destroy the object. """
		self.destroy()


class Collider(Wrapper):
	""" The sprite that could move around the graphic screen and be destroyed. """
	def update(self):
		""" Check if there are sprites visaully overlapping the given one. """
		super().update()
		if self.overlapping_sprites:
			for sprite in self.overlapping_sprites:
				sprite.die()
			self.die()

	def die(self):
		""" Destroy the object with explosion. """
		new_explosion = Explosion(x=self.x, y=self.y)
		games.screen.add(new_explosion)
		self.destroy()


class Asteroid(Wrapper):
	""" An asteroid moving in a straight line across the screen. """
	SMALL = 1
	MEDIUM = 2
	LARGE = 3
	images = {SMALL: games.load_image("asteroid_small.bmp"),
			  MEDIUM: games.load_image("asteroid_medium.bmp"),
			  LARGE: games.load_image("asteroid_large.bmp")}
	SPEED = 2
	SPAWN = 2

	def __init__(self, x, y, size):
		""" Initialize a sprite with the asteroid picture. """
		super().__init__(
				image=Asteroid.images[size],
				x=x,
				y=y,
				dx=random.choice([-1, 1]) * Asteroid.SPEED * random.random()/size,
				dy=random.choice([-1, 1]) * Asteroid.SPEED * random.random()/size)
		self.size = size

	def die(self):
		""" Destroy the asteroid. """
		# If the size of asteroid is large or middle, 
		# replace it with SPAWN=2 smaller ones.
		if self.size != Asteroid.SMALL:
			for i in range(Asteroid.SPAWN):
				new_asteroid = Asteroid(
						x=self.x,
						y=self.y,
						size=self.size-1)
				games.screen.add(new_asteroid)
		super().die()


class Ship(Collider):
	""" Player's ship. """
	IMAGE = games.load_image("ship.bmp")
	SOUND = games.load_sound("thrust.wav")
	ROTATION_STEP = 3
	VELOCITY_STEP = 0.03
	# It could be launched 2 missile per second.
	MISSILE_DELAY = 25

	def __init__(self, x, y):
		""" Initialize the sprite with spaceship picture. """
		super().__init__(
			image=Ship.IMAGE,
			x=x,
			y=y)
		self.missile_wait = 0

	def update(self):
		""" Rotate the ship when arrow keys is pressed. """
		if games.keyboard.is_pressed(games.K_LEFT):
			self.angle -= Ship.ROTATION_STEP
		if games.keyboard.is_pressed(games.K_RIGHT):
			self.angle += Ship.ROTATION_STEP
		
		# The ship makes a jerk.
		if games.keyboard.is_pressed(games.K_UP):
			Ship.SOUND.play()
			# Convert degrees to radians.
			angle = self.angle * math.pi / 180
			self.dx += Ship.VELOCITY_STEP * math.sin(angle)
			self.dy += Ship.VELOCITY_STEP * -math.cos(angle)

		# If the Space is pressed and waiting interval is ended, launch a missile.
		if games.keyboard.is_pressed(games.K_SPACE) and 0 == self.missile_wait:
			new_missile = Missile(self.x, self.y, self.angle)
			games.screen.add(new_missile)
			self.missile_wait = Ship.MISSILE_DELAY

		# If the next missile is not yet authorized to launch, 
		# subtract 1 from the length of the remaining waiting interval.	
		if self.missile_wait > 0:
			self.missile_wait -= 1

		# The ship will go around the screen.
		# Check if the sprite overlaps with another ones.
		super().update()


class Missile(Collider):
	""" Missile that the player's spaceship could launch.  """
	IMAGE = games.load_image("missile.bmp")
	SOUND = games.load_sound("missile.wav")
	BUFFER = 70
	VELOCITY_FACTOR = 7
	LIFETIME = 40

	def __init__(self, ship_x, ship_y, ship_angle):
		""" Initialize a sprite with image of a missile. """
		Missile.SOUND.play()
		
		# Convert degrees to radians.
		angle = ship_angle * math.pi / 180
		# Calculate the start position of the missile.
		buffer_x = Missile.BUFFER * math.sin(angle)
		buffer_y = Missile.BUFFER * -math.cos(angle)
		x = ship_x + buffer_x
		y = ship_y + buffer_y

		# Calculate horizontal and vertical velocity of the missile.
		dx = Missile.VELOCITY_FACTOR * math.sin(angle)
		dy = Missile.VELOCITY_FACTOR * -math.cos(angle)

		# Create the missile.
		super().__init__(
				image=Missile.IMAGE,
				x=x,
				y=y,
				dx=dx,
				dy=dy)
		self.lifetime = Missile.LIFETIME

	def update(self):
		""" Move the missile. """
		# If the missile has "expired", it is destroyed.
		self.lifetime -= 1
		if 0 == self.lifetime:
			self.destroy()

		# The rocket will go around the screen.
		# Check if the sprite overlaps with another ones.
		super().update()


class Explosion(games.Animation):
	""" Animation explosion. """
	SOUND = games.load_sound("explosion.wav")
	IMAGES = [
			"explosion1.bmp",
			"explosion2.bmp",
			"explosion3.bmp",
			"explosion4.bmp",
			"explosion5.bmp",
			"explosion6.bmp",
			"explosion7.bmp",
			"explosion8.bmp",
	]

	def __init__(self, x, y):
		super().__init__(
				images=Explosion.IMAGES,
				x=x,
				y=y,
				repeat_interval=4,
				n_repeats=1,
				is_collideable=False)
		Explosion.SOUND.play()


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
			x=games.screen.width/2,
			y=games.screen.height/2)
	games.screen.add(the_ship)
	
	# Start the main event loop.
	games.screen.mainloop()

# Go!
if "__main__" == __name__:
	main()
