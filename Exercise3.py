# Prompt user to enter the total square feet in a tract of land
totalSqFt = int(input('Enter the total square feet of land: '))

# Calculate the total square feet divided by 43560 to get the number of acres
acres = totalSqFt / 43560

# Display the number of acres
print(f'Number of acres is {acres:.2f}')