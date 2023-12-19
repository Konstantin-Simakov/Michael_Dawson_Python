# bouncing_pizza.py
# Demonstrates how to handle collisions with screen boundaries.

from superwires import games

games.init(screen_width=640, screen_height=480, fps=50)

class Pizza(games.Sprite):
	""" Bouncing pizza. """
	def update(self):
		""" 
		Reverse one or both velocity components 
		if a screen boundary is reached. 
		"""
		if self.right > games.screen.width or self.left < 0:
			self.dx = -self.dx;
		if self.bottom > games.screen.height or self.top < 0:
			self.dy = -self.dy;

def main():
	wall_image = games.load_image("wall.jpg", transparent=False)
	games.screen.background = wall_image

	pizza_image = games.load_image("pizza.bmp")
	the_pizza = Pizza(
			image=pizza_image,
			x=games.screen.width/2,
			y=games.screen.height/2,
			dx=1,
			dy=1)
	games.screen.add(the_pizza)

	games.screen.mainloop()

# Go!
if "__main__" == __name__:
	main()
