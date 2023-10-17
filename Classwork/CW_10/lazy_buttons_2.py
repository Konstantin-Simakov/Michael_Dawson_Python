# lazy_buttons_2.py
# Demonstrates creating a class in window app based on tkinter module.

from tkinter import *

class Application(Frame):
	""" A GUI application with three buttons. """
	def __init__(self, master):
		""" Initialize a frame. """
		super().__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		""" Create three lazy buttons. """
		
		# First button.
		self.bttn_1 = Button(self, text="I do nothing!")
		self.bttn_1.grid()

		# Second button.
		self.bttn_2 = Button(self)
		self.bttn_2.grid()
		self.bttn_2.configure(text="And me too!")

		# Third button.
		self.bttn_3 = Button(self)
		self.bttn_3.grid()
		self.bttn_3["text"] = "And me!"


# Main part.
root = Tk()
root.title("Lazy buttons - 2")
root.geometry("200x100")

app = Application(root)

root.mainloop()

