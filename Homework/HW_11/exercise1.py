# exercise1.py
# 
# Improve the 'Pizza panic' (pizza_panic.py) program.
# Increase a difficult level by:
# 1) increasing the falling speed of a pizza circle and/or
# 2) moving the chef faster, 
# 3) decreasing the distance between the pan and the roof, and for last,
# 4) releasing more crazy chefs.
# 

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
				# 3. Decrease the distance between the pan and the roof.
				bottom=games.screen.height-150)

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
	# 1. Increase the falling speed of a pizza circle
	# (speed -> 3 instead of 2).
	speed = 3

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
	IMAGE = games.load_image("chef.bmp")
	
	# 2. Move the chef faster (speed -> 5 instead of 2).
	def __init__(self, y=55, speed=5, odds_change=200):
		""" Initialize a Chef object. """
		super().__init__(
				image=Chef.IMAGE,
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

	# 4. Release more crazy chefs by creating a list of them
	# and adding them on the graphics screen.
	# the_chef = Chef()
	# games.screen.add(the_chef)
	crazy_chefs = []
	for i in range(3):
		crazy_chefs.append(Chef())
		games.screen.add(crazy_chefs[i])
	# Create a pan next.
	the_pan = Pan()
	games.screen.add(the_pan)

	games.mouse.is_visible = False
	games.screen.event_grab = True
	games.screen.mainloop()

# Go!
if "__main__" == __name__:
	main()
