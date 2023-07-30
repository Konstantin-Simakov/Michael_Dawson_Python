# exercise2.py
# 
# The program imitates the TV as an object.
# User can enter a channel number and increase/reduse the volume.
# 


MAX_CHANNEL = 100
MAX_VOLUME = 10


class Televisor(object):
	'''Imitates a TV.'''

	def __init__(self, channel=1, volume=(MAX_VOLUME // 2)):
		self.__channel = channel
		self.__volume = volume

	def __str__(self):
		res = "\n"
		res += "Your channel: " + str(self.__channel) + "\n"
		res += "Your volume: " + str(self.__volume) + "\n"

		return res

	def select_channel(self):
		channel = int(input("Enter a channel number: "))
		while channel < 0 or channel > MAX_CHANNEL:
			print("Incorrect channel number has been entered. Try again.")
			channel = int(input("Enter a channel number: "))

		print("Ok...")
		self.__channel = channel

	def volume_up(self):
		self.__volume += 1
		if self.__volume > MAX_VOLUME:
			self.__volume = MAX_VOLUME
		print("Ok.")

	def volume_down(self):
		self.__volume -= 1
		if self.__volume < 0:
			self.__volume = 0
		print("Ok.")


# Main part
def main():
	print("\t\tWelcome to the TV imitation program!\n")
	print("\t\tChannels: 1 -", MAX_CHANNEL)
	print("\t\tVolume levels: 1 -", MAX_VOLUME, "\n")
	
	tv = Televisor()
	print(tv)

	choice = None
	while choice != "0":
		print(
			"""
		0 - Quit
		1 - Display status
		2 - Select channel number
		3 - Up volume level
		4 - Down volume level
			"""
		)
		choice = input("Your choice: ")
		print()

		if "0" == choice:
			print("Bye.")
		elif "1" == choice:
			print(tv)
		elif "2" == choice:
			tv.select_channel()
		elif "3" == choice:
			tv.volume_up()
		elif "4" == choice:
			tv.volume_down()
		else:
			print("Sorry, there is no item", choice, "in the menu.")


# Start the program
main()
input("\n\nPress the key <Enter> to exit.")
