# Learn about slicing funtion in python
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

# Print keys from position 2 to position 5. This will give the keys c, d, e
print("Piano keys between positions 2 and 5")
print(piano_keys[2:5])
print()

#  Print keys from position 2 onwards
print("Piano keys from position 2 onwards")
print(piano_keys[2:])
print()

# Print all keys before position 4
print("Piano keys before position 2")
print(piano_keys[:4])
print()

# Print keys from position 1 with an increment or step of 2
print("Piano keys that start from position 1 and have a step of 2")
print(piano_keys[1:7:2])
print()

# Print every second key in the list
print("Printint every second key in the Piano keys")
print(piano_keys[::2])
print()

# Print all keys in the piano keys in the reverse direction
print("Printing all piano keys in the reverse direction")
print(piano_keys[::-1])
print()

# Print every other key (increments of 2) in the reverse direction
print("Printing every other key in the revers direction")
print(piano_keys[::-2])

# Slcicing in tuples
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
print("Print the items from position 2 to 5 of a tuple")
print(piano_tuple[2:5])

