# pickle_it.py
# 
# Demonstrates data pickling and 
# access through the shelve interface.
# 

import pickle, shelve

# 1
print("Pickle lists.")
variety = ["cucumbers", "tomatoes", "cabbage"]
shape = ["whole", "diced", "straw"]
brand = ["Main Product", "Chumak", "Bonduel"]
bin_file = open("pickle_1.dat", "wb+")
pickle.dump(variety, bin_file)
pickle.dump(shape, bin_file)
pickle.dump(brand, bin_file)
# bin_file.close()

print("\nUnpickle lists.")
bin_file.seek(0)                                # Return to the beginning of the file without closing it.
# bin_file = open("pickle_1.dat", "rb")
variety = pickle.load(bin_file)
shape = pickle.load(bin_file)
brand = pickle.load(bin_file)
print(variety)
print(shape)
print(brand)
bin_file.close()

# 2
print("\nShelve lists.")
# Read and write, create the file if it doesn't exist.
# sh = shelve.open("pickle_2.dat", "c")         # "c" == "ab+", "n" == "wb+", "r" == "rb", "w" == "ab"
sh = shelve.open("pickle_2.dat")
sh["variety"] = ["cucumbers", "tomatoes", "cabbage"]
sh["shape"] = ["whole", "diced", "straw"]
sh["brand"] = ["Main product", "Chumak", "Bonduel"]
# Make sure data is put down
sh.sync()

print("\nUnshelve lists.")
print("Brands -", sh["brand"])
print("Shapes -", sh["shape"])
print("Varieties -", sh["variety"])
sh.close()

input("\n\nPress the key <Enter> to exit.")
