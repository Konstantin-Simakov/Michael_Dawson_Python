# exercise3.py
# 
# Create a simple ping pong game for one player. 
# In this game, the user must control the racket, 
# and the ball must bounce off three walls. 
# If the ball misses the racket and flies out of the playing field, 
# the game must end.
# 

from superwires import games, color
import random

games.init(screen_width=550, screen_height=365, fps=50)

class Ball(games.Sprite):
	""" A ball in ping pong game. """
	IMAGE = games.load_image("ball.bmp")
	SPEED = 3

	def __init__(self):
		super().__init__(
				image=Ball.IMAGE,
				x=games.screen.width/2,
				y=games.screen.height/2,
				dx=Ball.SPEED,
				dy=Ball.SPEED)

	def update(self):
		""" 
		Reverse one or both velocity components 
		if a screen boundary or a racket is reached. 
		"""
		if self.left < 0 or self.right > games.screen.width:
			self.dx = -self.dx
		if self.top < 0:
			self.dy = -self.dy
		if self.bottom > games.screen.height:
			self.end_game()
			self.destroy()

	def end_game(self):
		""" Finish the game. """
		end_message = games.Message(
				value="Game Over",
				size=70,
				color=color.red,
				x=games.screen.width/2,
				y=games.screen.height/2,
				lifetime=3*games.screen.fps,
				after_death=games.screen.quit)
		games.screen.add(end_message)

	def handle_hit(self):
		""" Bounce off the racket in a vertical direction. """
		self.dy = -self.dy

class Racket(games.Sprite):
	""" A racket that user plays with. """
	IMAGE = games.load_image("racket.png")

	def __init__(self):
		super().__init__(
				image=Racket.IMAGE,
				x=games.mouse.x,
				y=games.screen.height-50)

	def update(self):
		""" 
		Move the object horizontally to a point with 
		an abscissa equal to the mouse pointer. 
		"""
		self.x = games.mouse.x
		if self.left < 0:
			self.left = 0
		elif self.right > games.screen.width:
			self.right = games.screen.width
		self.check_hit()

	def check_hit(self):
		""" Check if the ball is hit by the racket. """
		for ball in self.overlapping_sprites:
			ball.handle_hit()

def main():
	""" Main program. """
	# Set the screen background.
	ping_pong_image = games.load_image("ping_pong.png", transparent=False)
	games.screen.background = ping_pong_image

	the_ball = Ball()
	games.screen.add(the_ball)
	the_racket = Racket()
	games.screen.add(the_racket)
	
	games.mouse.is_visible = False
	games.screen.event_grab = True
	games.screen.mainloop()

# Go!
if "__main__" == __name__:
	main()
