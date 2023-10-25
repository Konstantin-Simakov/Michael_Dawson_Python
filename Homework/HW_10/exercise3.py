# exercise3.py
#  
# The "Check please" program.
# The program displays a simple restaurant menu with dishes and prices, 
# acceapts the user's order and displays the bill amount.
#  

from tkinter import *

class Application(Frame):
    """ The GUI app that implements the given above task. """
    def __init__(self, master):
        """ Initialize the frame. """
        super().__init__(master)
        self.grid()

        self.create_widgets()

    def create_widgets(self):
        """ Create and place all GUI control elements. 
            Displays menu (dishes) and prices.
        """
        # Instcutions label.
        text = "\t\tWelcome to the \'Check please\' program!\n"
        text += "\t\tPlace your order:\n"
        row = 0
        Label(self, text=text).grid(row=row, column=0, sticky=W, columnspan=2)
        row += 1

        # First dish.
        # ---------------------------------------------------------------------
        text = "What will you have first?"
        Label(self, text=text).grid(row=row, column=0, sticky=W)
        row += 1
        
        # Display and choose the first dish.
        first_dishes = ["Borsch", "Cabbage soup", "Chicken soup", "Fish soup"]
        first_prices = [1500, 1300, 1100, 1200]
        self.first = IntVar()
        self.first.set(0)
        temp = row
        for i in range(len(first_dishes)):
            r_b = Radiobutton(self, text=first_dishes[i], variable=self.first, value=first_prices[i], command=self.update_count)
            r_b.grid(row=row, column=0, sticky=W)
            row += 1
        # Display first dish prices.
        row = temp
        for price in first_prices:
            lbl = Label(self, text=("$" + str(price)))
            lbl.grid(row=row, column=1, sticky=W)
            row += 1
        # ---------------------------------------------------------------------

        # Second dish.
        # ---------------------------------------------------------------------
        text = "What will you have second?"
        Label(self, text=text).grid(row=row, column=0, sticky=W)
        row += 1

        # Display and choose the second dish.
        second_dishes = ["Pasta with chicken", "Buckwheat with meat", "Rice with fish"]
        second_prices = [1200, 1300, 1400]
        self.second = IntVar()
        self.second.set(0)
        temp = row
        for i in range(len(second_dishes)):
            r_b = Radiobutton(self, text=second_dishes[i], variable=self.second, value=second_prices[i], command=self.update_count)
            r_b.grid(row=row, column=0, sticky=W)
            row += 1
        # Display the second dish prices.
        row = temp
        for price in second_prices:
            lbl = Label(self, text=("$" + str(price)))
            lbl.grid(row=row, column=1, sticky=W)
            row += 1
        # ---------------------------------------------------------------------

        # Salad.
        # ---------------------------------------------------------------------
        text = "What will you have for salad?"
        Label(self, text=text).grid(row=row, column=0, sticky=W)
        row += 1

        # Display and choose a salad.
        salads = ["Crab salad", "Olivie", "Greek salad"]
        salad_prices = [1000, 1100, 1200]
        self.salad = IntVar()
        self.salad.set(0)
        temp = row
        for i in range(len(salads)):
            r_b = Radiobutton(self, text=salads[i], variable=self.salad, value=salad_prices[i], command=self.update_count)
            r_b.grid(row=row, column=0, sticky=W)
            row += 1

        # Display salad prices.
        row = temp
        for price in salad_prices:
            lbl = Label(self, text=("$" + str(price)))
            lbl.grid(row=row, column=1, sticky=W)
            row += 1
        # ---------------------------------------------------------------------

        # Drinks.
        # ---------------------------------------------------------------------
        text = "What will you have for drink(s)?"
        Label(self, text=text).grid(row=row, column=0, sticky=W)
        row += 1

        # Display and choose drink(s).
        drinks = ["Black tea", "Green tea", "Cappuccino", "Black coffee", "Lemon tea"]
        self.drink_prices = [1000, 1100, 1200, 1300, 1500]
        self.bool_drinks = []
        temp = row
        for i in range(len(drinks)):
            self.bool_drinks.append(BooleanVar())
            c_b = Checkbutton(self, text=drinks[i], variable=self.bool_drinks[i], command=self.update_count)
            c_b.grid(row=row, column=0, sticky=W)
            row += 1

        # Display drink prices.
        row = temp
        for price in self.drink_prices:
            lbl = Label(self, text=("$" + str(price)))
            lbl.grid(row=row, column=1, sticky=W)
            row += 1
        # ---------------------------------------------------------------------

        # Desserts.
        # ---------------------------------------------------------------------
        text = "What will you have for dessert(s)?"
        Label(self, text=text).grid(row=row, column=0, sticky=W)
        row += 1

        # Display and choose dessert(s).
        desserts = ["Pancakes", "Apple pie", "Blackcurrant muffins", "Chocolate cake"]
        self.dessert_prices = [1000, 1100, 1200, 1300]
        self.bool_desserts = []
        temp = row
        for i in range(len(desserts)):
            self.bool_desserts.append(BooleanVar())
            c_b = Checkbutton(self, text=desserts[i], variable=self.bool_desserts[i], command=self.update_count)
            c_b.grid(row=row, column=0, sticky=W)
            row += 1

        # Display dessert prices.
        row = temp
        for price in self.dessert_prices:
            lbl = Label(self, text=("$" + str(price)))
            lbl.grid(row=row, column=1, sticky=W)
            row += 1
        # ---------------------------------------------------------------------
        
        # Count.
        # ---------------------------------------------------------------------
        self.count_txt = Text(self, width=50, height=50, wrap=WORD)
        self.count_txt.grid(row=row, column=0, sticky=W)
        row += 1
        # ---------------------------------------------------------------------

    def update_count(self):
        """ Update the count based on dish prices. """
        sum_check = 0
        # Sum all values of radio buttons.
        sum_check += self.first.get() + self.second.get() + self.salad.get()
        
        # Sum all values of check buttons.
        # Drinks.
        for i in range(len(self.drink_prices)):
            if self.bool_drinks[i].get():
                sum_check += self.drink_prices[i]

        # Desserts.
        for i in range(len(self.dessert_prices)):
            if self.bool_desserts[i].get():
                sum_check += self.dessert_prices[i]

        # Update (display) the text count.
        sum_message = "The sum of your order is $" + str(sum_check)
        self.count_txt.delete(0.0, END)
        self.count_txt.insert(0.0, sum_message)


# Main program.
root = Tk()
root.title("Check please")
app = Application(root)
root.mainloop()
