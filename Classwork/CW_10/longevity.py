# longevity.py
# Demonstrates text field (Entry), text area (Text) and Grid layout manager.

from tkinter import *

class Application(Frame):
	""" GUI app holding the secret to longevity. """
	def __init__(self, master):
		""" Initialize the frame. """
		super().__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		""" Create a button, text field and text area. """
		
		# Instruction label.
		self.inst_lbl = Label(self, text="To find out the longevity secret, enter the password.")
		self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)

		# Password label.
		self.pw_lbl = Label(self, text="Password: ")
		self.pw_lbl.grid(row=1, column=0, sticky=W)

		# Text area to password input.
		self.pw_ent = Entry(self)
		self.pw_ent.grid(row=1, column=1, sticky=W)

		# Submit button.
		self.submit_bttn = Button(self, text="Find out the secret", command=self.reveal)
		self.submit_bttn.grid(row=2, column=0, sticky=W)

		# Create a text area where the answer will be displayed in.
		self.secret_text = Text(self, width=35, height=5, wrap=WORD)
		self.secret_text.grid(row=3, column=0, columnspan=2, sticky=W)

	def reveal(self):
		""" Display the message depend on the input password. """
		contents = self.pw_ent.get()
		if "secret" == contents:
			message = "To live to be 100 years, you should live first to 99, " \
					"and then be VERY careful."
		else:
			message = "You entered the incorrect password, so I can\'t " \
					"share the secret with you."

		self.secret_text.delete(0.0, END)
		self.secret_text.insert(0.0, message)


# Main part.
root = Tk()
root.title("Longevity")
root.geometry("300x200")
app = Application(root)
root.mainloop()
