# Python uses lists instead of traditional arrays.

# Create a list of colours
colours = ["Blue", "Green", "Red", "Yellow", "Orange"]

# Add a new colour to the end of the list
colours.append("Cyan")
print(colours)

# Insert a colour at position 1
colours.insert(1, "Purple")
print(colours)

# Remove a colour from the list
colours.remove("Green")
print(colours)

# Print the number of items in the list
print(len(colours))

# Count how many times "Blue" appears in the list
print(colours.count("Blue"))

# Loop through and print each colour
for colour in colours:
    print(colour)
