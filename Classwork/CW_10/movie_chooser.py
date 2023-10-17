# movie_chooser.py
# Demonstrates using flags.

from tkinter import *

class Application(Frame):
    """ GUI app letting to choose favourite movie genres. """
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create elements that the user will use to choose. """

        # Description label.
        Label(self, 
                text="Specify your favourite movie genres."
        ).grid(row=0, column=0, sticky=W)

        # Instructions label.
        Label(self,
                text="Choose all you like:"
        ).grid(row=1, column=0, sticky=W)

        # Flag "Comedy".
        self.likes_comedy = BooleanVar()
        Checkbutton(self,
                text="Comedy",
                variable=self.likes_comedy,
                command=self.update_text
        ).grid(row=2, column=0, sticky=W)

        # Flag "Drama".
        self.likes_drama = BooleanVar()
        Checkbutton(self,
                text="Drama",
                variable=self.likes_drama,
                command=self.update_text
        ).grid(row=3, column=0, sticky=W)

        # Flag "Romance".
        self.likes_romance = BooleanVar()
        Checkbutton(self,
                text="Romance",
                variable=self.likes_romance,
                command=self.update_text
        ).grid(row=4, column=0, sticky=W)

        # Text area (Text) with results.
        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        """ Update the text element according to user choose. """
        likes = ""
        if self.likes_comedy.get():
            likes += "You like comedies.\n"
        if self.likes_drama.get():
            likes += "You like drama genre.\n"
        if self.likes_romance.get():
            likes += "You like romance movie.\n"
        
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, likes)


# Main part.
root = Tk()
root.title("Movie chooser")
app = Application(root)
root.mainloop()
