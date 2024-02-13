# sound_and_music.py
# Demonstrate playing sounds and music files.

from superwires import games

games.init(screen_width=640, screen_height=480, fps=50)

# Load a sound file.
missile_sound = games.load_sound("missile.wav")

# Load a music file.
games.music.load("theme.mid")

choice = None
while choice != "0":
	print(
	"""
	Sound and music.
	0 - Quit
	1 - Play missile sound
	2 - Cycle missile sound
	3 - Stop missile sound
	4 - Play game theme music
	5 - Cycle game theme music
	6 - Stop game theme music
	"""
	)
	choice = input("Your choice: ")
	print()

	# Quit.
	if "0" == choice:
		print("Good-bye.")
	
	# Play missile sound.
	elif "1" == choice:
		missile_sound.play()
		print("Play missile sound.")

	# Cycle missile sound.
	elif "2" == choice:
		loop = int(input("How many more times to play this sound? (-1 = play endless): "))
		missile_sound.play(loop)
		print("Cycle missile sound.")

	# Stop missile sound.
	elif "3" == choice:
		missile_sound.stop()
		print("Stop missile sound.")

	# Play game theme music.
	elif "4" == choice:
		games.music.play()
		print("Play game theme music.")

	# Cycle game theme music.
	elif "5" == choice:
		loop = int(input("How many more times to play this music? (-1 = play endless): "))
		games.music.play(loop)
		print("Cycle game theme music.")

	# Stop game theme music.
	elif "6" == choice:
		games.music.stop()
		print("Stop game theme music.")

	# Unknown user input.
	else:
		print("Sorry, there is no point", choice, "in the menu.")

input("\n\nPress the key <Enter> to exit.")
