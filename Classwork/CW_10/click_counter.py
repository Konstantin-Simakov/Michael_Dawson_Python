# click_counter.py
# Demonstrates binding events with processors.

from tkinter import *

class Application(Frame):
	""" A GUI app counting a number of button clicks. """
	def __init__(self, master):
		""" Initialize the frame. """
		super().__init__(master)
		self.grid()
		# The number of clicks.
		self.bttn_clicks = 0
		self.create_widgets()

	def create_widgets(self):
		""" Create a button that displays the number of clicks made. """
		self.bttn = Button(self)
		self.bttn["text"] = "Number of clicks: 0"
		self.bttn["command"] = self.update_count
		self.bttn.grid()

	def update_count(self):
		""" Increase the number of clicks by one and display it. """
		self.bttn_clicks += 1
		self.bttn["text"] = "Number of clicks: " + str(self.bttn_clicks)


# Main part.
root = Tk()
root.title("Number of clicks")
root.geometry("250x100")

app = Application(root)

root.mainloop()
