# pizza_panic.py
# The player must catch the falling pizza before it reaches the ground.

from superwires import games, color
import random

games.init(screen_width=640, screen_height=480, fps=50)

class Pan(games.Sprite):
	"""  
	A pan in which the player could catch the falling pizza.
	"""
	image = games.load_image("pan.bmp")

	def __init__(self):
		""" 
		Initialize a Pan object and create a Text object for displaying the counter. 
		"""
		super().__init__(
				image=Pan.image,
				x=games.mouse.x,
				bottom=games.screen.height)

		self.score = games.Text(
				value=0, 
				size=25, 
				color=color.black,
				top=5, 
				right=games.screen.width)
		games.screen.add(self.score)

	def update(self):
		""" 
		Move the object horizontally to a point with an abscissa equal to the mouse pointer.			
		"""
		self.x = games.mouse.x
		if self.left < 0:
			self.left = 0
		if self.right > games.screen.width:
			self.right = games.screen.width
		self.check_catch()

	def check_catch(self):
		""" Check if the player catches a falling pizza. """
		for pizza in self.overlapping_sprites:
			self.score.value += 10
			self.score.right = games.screen.width - 10
			pizza.handle_caught()

class Pizza(games.Sprite):
	"""
	Pizza circles falling to the ground.
	"""
	image = games.load_image("pizza.bmp")
	speed = 1

	def __init__(self, x, y=90):
		""" Initialize a Pizza object. """
		super().__init__(
				image=Pizza.image,
				x=x,
				dy=Pizza.speed)

	def update(self):
		""" 
		Checks to see if the bottom edge of the sprite is 
		touching the bottom edge of the screen. 
		"""
		if self.bottom > games.screen.height:
			self.end_game()
			self.destroy()

	def handle_caught(self):
		""" Destroy the object that the player caught. """
		self.destroy()

	def end_game(self):
		""" Finsih the game. """
		end_message = games.Message(
				value="Game Over",
				size=90,
				color=color.red,
				x=games.screen.width/2,
				y=games.screen.height/2,
				lifetime=5*games.screen.fps,
				after_death=games.screen.quit)
		games.screen.add(end_message)

class Chef(games.Sprite):
	"""
	A chef who throws pizza around, moving left and right.
	"""
	image = games.load_image("chef.bmp")
	
	def __init__(self, y=55, speed=2, odds_change=200):
		""" Initialize a Chef object. """
		super().__init__(
				image=Chef.image,
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
		drop next pizza and recover the origin interval.
		"""
		if self.time_til_drop > 0:
			self.time_til_drop -= 1
		else:
			new_pizza = Pizza(x=self.x)
			games.screen.add(new_pizza)
			# Regardless of the speed at which the pizza falls, 
			# the “gap” between the falling circles is assumed 
			# to be equal to 30% of each of them.
			self.time_til_drop = int(new_pizza.height * 1.3 / Pizza.speed) + 1

def main():
	""" The actual gameplay. """
	wall_image = games.load_image("wall.jpg", transparent=False)
	games.screen.background = wall_image

	the_chef = Chef()
	games.screen.add(the_chef)
	the_pan = Pan()
	games.screen.add(the_pan)

	games.mouse.is_visible = False
	games.screen.event_grab = True
	games.screen.mainloop()

# Go!
if "__main__" == __name__:
	main()
