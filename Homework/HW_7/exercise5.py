# exercise5.py
# 
# File compression function.
# The program compresses a source text file 
# and outputs it to the target text file.
# The file input.txt must be existed.
# The file output.txt will be existed.
# 


def display_file(the_file):
	'''Displays the all content of the file.'''
	print(the_file.read())


def compress_file(input_file, output_file):
	'''Compresses the input file into the output file.'''
	# Read characters.
	count = 0

	# Character-by-character reading of a file.
	# Target loop.
	# input_ch is one character from the input text file.
	input_ch = input_file.read(1)
	# output_text is a result string. 
	output_text = ""
	while input_ch:
		if count % 3 == 0:
			output_text += input_ch
		count += 1
		input_ch = input_file.read(1)
	
	# Finishing output_text string.
	output_text += "\n"
	output_file.write(output_text)


def main():
	'''Main program.'''
	# Openingn of files.
	input_file = open("input.txt", "r", encoding="utf-8")
	output_file = open("output.txt", "w+", encoding="utf-8")

	# Displaying of a source file.
	display_file(input_file)
	
	# Processing of files.
	# Move the cursor to the beginning of the source file.
	input_file.seek(0)
	compress_file(input_file, output_file)
	
	# Displyaing of a target file.
	# Move the cursor to the beginning of the target file.
	output_file.seek(0)
	display_file(output_file)
	
	# Closing of files.
	output_file.read()
	output_file.close()
	

main()
input("\n\nPress the key <Enter> to exit.")
