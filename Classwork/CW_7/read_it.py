# read_it.py
# Demonstrates reading from a text file

print("Open and close file.")
text_file = open("read_it.txt", "r", encoding="utf-8")
text_file.close()

print("\nRead file character by character.")
text_file = open("read_it.txt", "r", encoding="utf-8")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print("\nRead entire file.")
text_file = open("read_it.txt", "r", encoding="utf-8")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

print("\nRead one line character by character.")
text_file = open("read_it.txt", "r", encoding="utf-8")
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()

print("\nRead one entire line.")
text_file = open("read_it.txt", "r", encoding="utf-8")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print("\nRead entire file to list.")
text_file = open("read_it.txt", "r", encoding="utf-8")
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
	print(line)
text_file.close()

print("\nRead file line by line.")
text_file = open("read_it.txt", "r", encoding="utf-8")
for line in text_file:
	print(line)
text_file.close()

input("\n\nPress the key <Enter> to exit.")
