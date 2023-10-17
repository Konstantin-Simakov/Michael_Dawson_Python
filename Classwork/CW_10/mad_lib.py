# mad_lib.py
# Create a story based on user input.

from tkinter import *

class Application(Frame):
    """ GUI app creating a story based on user input. """
    def __init__(self, master):
        """ Initialize the frame. """
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create control elements with which 
            the user will enter source data and get a full story. 
        """
        # Instructions label.
        Label(self, 
                text="Enter data for creating a new story.",
        ).grid(row=0, column=0, columnspan=2, sticky=W)

        # Label and entry for a person name.
        Label(self,
                text="Person name:",
        ).grid(row=1, column=0, sticky=W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row=1, column=1, sticky=W)

        # Label and entry for a noun.
        Label(self,
                text="Plural noun:"
        ).grid(row=2, column=0, sticky=W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row=2, column=1, sticky=W)

        # Label and entry for a verb.
        Label(self, 
                text="Verb in infinitive:",
        ).grid(row=3, column=0, sticky=W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row=3, column=1, sticky=W)

        # Label for a group of flags that are adjectives.
        Label(self,
                text="Adjective(s):",
        ).grid(row=4, column=0, sticky=W)
        
        # "Itchy" flag.
        self.is_itchy = BooleanVar()
        Checkbutton(self,
                text="itchy",
                variable=self.is_itchy,
        ).grid(row=4, column=1, sticky=W)

        # "Joyous" flag.
        self.is_joyous = BooleanVar()
        Checkbutton(self,
                text="joyous",
                variable=self.is_joyous
        ).grid(row=4, column=2, sticky=W)

        # "Electric" flag.
        self.is_electric = BooleanVar()
        Checkbutton(self,
                text="electric",
                variable=self.is_electric
        ).grid(row=4, column=3, sticky=W)

        # Label for a radio button with body names.
        Label(self,
                text="Body part:",
        ).grid(row=5, column=0, sticky=W)

        # Variable consisting the name of one from body parts.
        self.body_part = StringVar()
        self.body_part.set(None)
        # Radio button with body parts.
        body_parts = ["navel", "big toe", "medulla oblongata"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                    text=part,
                    variable=self.body_part,
                    value=part
            ).grid(row=5, column=column, sticky=W)
            column += 1

        # Button of data sending.
        Button(self,
                text="Get a story",
                command=self.tell_story
        ).grid(row=6, column=0, sticky=W)

        self.story_txt = Text(self, width=75, height=10, wrap=WORD)
        self.story_txt.grid(row=7, column=0, columnspan=4)

    def tell_story(self):
        """ Fill text area one more story based on user input. """
        # Get values from the GUI.
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "itchy, " 
        if self.is_joyous.get():
            adjectives += "joyous, "
        if self.is_electric.get():
            adjectives += "electric, "

        body_part = self.body_part.get()

        # Create the story.
        story = "The famous traveler "
        story += person
        story += " has already dispair make the deal of his life - search of lost city where as legend says were "
        story += noun.title() + ". "
        
        story += "But once "
        story += noun
        story += " and "
        story += person + " come face up. "

        story += "Power, "
        story += adjectives
        story += "incomparable feel covered the soul of the traveler. "

        story += "After years for search, the goal was achieved at the end. "
        story += person
        story += " has felt a tear rolled down on his " + body_part + ". "
        story += "Suddenly "
        story += noun
        story += " go on the attack and "
        story += person + " was gobbled up immediately by them. "
        story += "Morality? If you decide to "
        story += verb + ", "
        story += "do it careful."

        # Output the story on the screen.
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)


# Main part.
root = Tk()
root.title("Mad librarian")
app = Application(root)
root.mainloop()
