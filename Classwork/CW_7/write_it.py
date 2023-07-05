# write_it.py
# Demonstrates writing to a text file

# 1st way
print("Create a new text file with write() method.")
text_file = open("write_it.txt", "w", encoding="utf-8")
text_file.write("Line 1\n")
text_file.write("It is line 2\n")
text_file.write("It is line with number 3\n")
text_file.close()

print("\nRead a newly created file.")
text_file = open("write_it.txt", "r", encoding="utf-8")
print(text_file.read())
text_file.close()

# 2nd way
# print("\nCreate a new text file with writelines() method.")
# text_file = open("write_it.txt", "w", encoding="utf-8")
# lines = [
# 	"Line 1\n",
# 	"It is line 2\n", 
# 	"It is line with number 3\n"
# ]
# text_file.writelines(lines)
# text_file.close()

# print("\nRead a newly created file.")
# text_file = open("write_it.txt", "r", encoding="utf-8")
# print(text_file.read())
# text_file.close()

input("\n\nPress the key <Enter> to exit.")
