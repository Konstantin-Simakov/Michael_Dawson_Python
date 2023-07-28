# constructor_critter.py
# Demonstrates constructor method.

class Critter(object):
    '''Virtual pet'''
    
    def __init__(self):
        print("The new critter has been born!")

    def talk(self):
        print("\nHello. I am a critter, an instance of Critter class.")


# Main part
crit_1 = Critter()
crit_2 = Critter()

crit_1.talk()
crit_2.talk()

input("\n\nPress the key <Enter> to exit.")
