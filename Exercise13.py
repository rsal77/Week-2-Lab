# Prompt user to enter vineyard and end-post assembly information
r = int(input('Enter the length of the row in feet: '))
e = int(input('Enter the amount of space used by end-post in feet: '))
s = int(input('Enter the amount of space between the vines in feet: '))

# Calculate the number of grapevines that will fit in a row
v = (r - 2 * e) / s

# Display the number of grapevines that will fit in a row
print(f'The number of grapevines per row is {v:.0f}')