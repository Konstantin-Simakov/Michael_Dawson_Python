# exercise2.py
# 
# The character, controlled by the player with the mouse, 
# dodges some heavy objects (bricks) falling from the "sky", and the player dodges.
# 

from superwires import games, color
import random

games.init(screen_width=725, screen_height=480, fps=50)

class Soldier(games.Sprite):
	""" A character that dodges. """
	IMAGE = games.load_image("soldier.bmp")

	def __init__(self):
		""" Initialize a soldier object. """
		super().__init__(
				image=Soldier.IMAGE,
				x=games.mouse.x,
				y=games.screen.height-50)

	def update(self):
		""" 
		Move the object horizontally to a point with an abscissa equal to the mouse pointer. 
		"""
		self.x = games.mouse.x
		if self.left < 0:
			self.left = 0
		if self.right > games.screen.width:
			self.right = games.screen.width
		self.check_collide()

	def check_collide(self):
		""" Check if the player cannot dodge from a falling brick. """
		for brick in self.overlapping_sprites:
			brick.handle_collide()

class Brick(games.Sprite):
	""" 
	A heavy thing that falls to the character (soldier). 
	"""
	IMAGE = games.load_image("brick.bmp")
	speed = 5

	def __init__(self, x, y=10):
		super().__init__(
				image=Brick.IMAGE,
				x=x,
				dy=Brick.speed)

	def update(self):
		"""
		Checks to see if the bottom edge of the sprite is 
		touching the bottom edge of the screen. 
		"""
		if self.bottom > games.screen.height:
			self.destroy()

	def handle_collide(self):
		""" End the game. """
		games.screen.clear()
		self.end_game()

	def end_game(self):
		""" Finish the game. """
		end_message = games.Message(
				value="Collided! Game over!",
				size=65,
				color=color.red,
				x=games.screen.width/2,
				y=games.screen.height/2,
				lifetime=3*games.screen.fps,
				after_death=games.screen.quit)
		games.screen.add(end_message)

class Dummy(games.Sprite):
	"""
	Invisible dummy from which the bricks are falling down.
	"""
	IMAGE = games.load_image("dummy.png")
	speed = 4.5
	
	def __init__(self, y=15, speed=speed, odds_change=200):
		""" Initialize a Chef object. """
		super().__init__(
				image=Dummy.IMAGE,
				x=games.screen.width/2,
				y=y,
				dx=speed)
		self.odds_change = odds_change
		self.time_til_drop = 0

	def update(self):
		""" Define if the direction needs to change. """
		if self.left < 0 or self.right > games.screen.width:
			self.dx = -self.dx
		elif 0 == random.randrange(self.odds_change):
			self.dx = -self.dx

		self.check_drop()

	def check_drop(self):
		"""
		Decrease expectation interval to 1 or 
		drop next brick and recover the origin interval.
		"""
		if self.time_til_drop > 0:
			self.time_til_drop -= 1
		else:
			# new_pizza = Pizza(x=self.x)
			new_brick = Brick(x=self.x)
			games.screen.add(new_brick)
			# Regardless of the speed at which the brick falls, 
			# the "gap" between the falling bricks is assumed 
			# to be equal to 4 sizes of each of them.
			self.time_til_drop = int(new_brick.height * 4 / Brick.speed) + 1


def main():
	""" The actual gameplay. """
	SKY_IMAGE = games.load_image("sky.jpg", transparent=False)
	games.screen.background = SKY_IMAGE

	games.screen.add(Dummy())

	# Create a soldier next.
	the_soldier = Soldier()
	games.screen.add(the_soldier)

	games.mouse.is_visible = False
	games.screen.event_grab = True
	games.screen.mainloop()

if "__main__" == __name__:
	main()
