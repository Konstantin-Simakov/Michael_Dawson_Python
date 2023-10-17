# movie_chooser_2.py
# Demonstrates radio buttons.

from tkinter import *

class Application(Frame):
    """ GUI app letting to choose one favourite movie genre. """
    def __init__(self, master):
        """ Initialize the frame. """
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create elements that the user will use to choose. """

        # Description label.
        Label(self,
                text="Specify your favourite movie genre."
        ).grid(row=0, column=0, sticky=W)

        # Instructions label.
        Label(self,
                text="Choose only one:"
        ).grid(row=1, column=0, sticky=W)

        # Variable for saving the information about the only favourite genre.
        self.favourite = StringVar()
        self.favourite.set(None)

        # Radio button "Comedy".
        Radiobutton(self,
                text="Comedy",
                variable=self.favourite,
                value="comedy",
                command=self.update_text
        ).grid(row=2, column=0, sticky=W)

        # Radio button "Drama"
        Radiobutton(self,
                text="Drama",
                variable=self.favourite,
                value="drama",
                command=self.update_text
        ).grid(row=3, column=0, sticky=W)

        # Radio button "Romance"
        Radiobutton(self,
                text="Romance",
                variable=self.favourite,
                value="romance",
                command=self.update_text
        ).grid(row=4, column=0, sticky=W)

        # Text area with results.
        self.results_text = Text(self, width=40, height=5, wrap=WORD)
        self.results_text.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        """ Update the text area, write to it the favourite genre. """
        message = "Your favourite genre is "
        message += self.favourite.get() + "."

        self.results_text.delete(0.0, END)
        self.results_text.insert(0.0, message)


# Main part.
root = Tk()
root.title("Movie chooser 2")
app = Application(root)
root.mainloop()
