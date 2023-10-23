# exercise2.py
# 
# Modify the program "Guess my number" (guess_my_number.py source file)
# by creating a GUI for it.
# 

from tkinter import *
import random

class Application(Frame):
	""" Create a special frame for guessing a number. """
	def __init__(self, master):
		""" Initialize the frame. """
		super().__init__(master)
		self.grid()
		self.create_widgets()
		# Computer guesses a number.
		self.the_number = random.randint(1, 100)
		print(self.the_number)
		# The number of attempts for guessing.
		self.tries = 0

	def create_widgets(self):
		""" Create control elelements. 
			(Count them and set parameters for them.)
		"""
		# Instructions label.
		text = "Welcome to Guess my number!\n"
		text += "\nI\'m thinking of a number between 1 and 100.\n"
		text += "Try to guess it in a few attempts as possible."
		lbl = Label(self, text=text)
		lbl.grid(row=0, column=1, columnspan=1, rowspan=3, sticky=W)

		# Label of the invitation for guess.
		text = "Take a guess:"
		lbl = Label(self, text=text)
		lbl.grid(row=4, column=0, sticky=W)
		# Entry for guessing attempt (only in two lines).
		self.ent = Entry(self)
		self.ent.grid(row=4, column=1, sticky=W)
		# Button to guess.
		self.bttn = Button(self, text="Guess", command=self.update_game_state)
		self.bttn.grid(row=5, column=0, sticky=W)

		# Output text after a guessing attempt.
		self.result_txt = Text(self, width=50, height=5, wrap=WORD)
		self.result_txt.grid(row=6, column=0, columnspan=5)

	def update_game_state(self):
		""" Update the output text after clicking on the button 'Guess' """
		self.tries += 1

		guess = self.ent.get()
		guess = int(guess)
		if self.the_number < guess:
			output_text = "Lower..."
		elif self.the_number > guess:
			output_text = "Higher..."
		else:
			output_text = "You guessed it! The number was " + str(self.the_number) + ".\n"
			output_text += "And it only took you " + str(self.tries) + " tries!\n"
			# Disable the ability clicking of the button 
			# and all control elements at all.
			self.bttn["state"] = DISABLED
			self.ent["state"] = DISABLED

		# Update the output text.
		self.result_txt.delete(0.0, END)
		self.result_txt.insert(0.0, output_text)
		if self.the_number == guess:
			self.result_txt["state"] = DISABLED


# Main program.
root = Tk()
root.title("Guess my number")
app = Application(root)
root.mainloop()
