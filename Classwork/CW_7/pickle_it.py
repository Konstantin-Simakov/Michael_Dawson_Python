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
f = open("picles_1.dat", "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("\nUnpickle lists.")
f = open("picles_1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
print(variety)
print(shape)
print(brand)
f.close()

# 2
print("\nShelve lists.")
# Read and write, create the file if it doesn't exist.
# s = shelve.open("pickle_2.dat", "c")
s = shelve.open("pickle_2.dat")
s["variety"] = ["cucumbers", "tomatoes", "cabbage"]
s["shape"] = ["whole", "diced", "straw"]
s["brand"] = ["Main product", "Chumak", "Bonduel"]
# Make sure data is put down
s.sync()

print("\nUnshelve lists.")
print("Brands -", s["brand"])
print("Shapes -", s["shape"])
print("Varieties -", s["variety"])
s.close()

input("\n\nPress the key <Enter> to exit.")
