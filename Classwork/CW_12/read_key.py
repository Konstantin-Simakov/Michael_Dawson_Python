# read_key.py
# Demonstrate key reading.

from superwires import games

games.init(screen_width=640, screen_height=480, fps=50)

class Ship(games.Sprite):
	""" Mobile spacecraft. """
	def update(self):
		""" Move the spaceship in a certain way based on the keys pressed. """
		if games.keyboard.is_pressed(games.K_w):
			self.y -= 1
		if games.keyboard.is_pressed(games.K_s):
			self.y += 1
		if games.keyboard.is_pressed(games.K_a):
			self.x -= 1
		if games.keyboard.is_pressed(games.K_d):
			self.x += 1


# Main program.
def main():
	nebula_image = games.load_image("nebula.jpg", transparent=False)
	games.screen.background = nebula_image

	ship_image = games.load_image("ship.bmp")
	the_ship = Ship(
			image=ship_image,
			x=games.screen.width/2,
			y=games.screen.height/2)
	games.screen.add(the_ship)

	games.screen.mainloop()

# Go!
if "__main__" == __name__:
	main()
