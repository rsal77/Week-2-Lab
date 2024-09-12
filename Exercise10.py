# Prompt user for the amount of cookies to be made
numOfCookies = int(input('Enter the number of cookies: '))

# List variable for the ingredients
cupsOfSugar = 1.5
cupsOfButter = 1
cupsOfFlour = 2.75

# Calculate the number for each ingredient
sugar = cupsOfSugar * numOfCookies
butter = cupsOfButter * numOfCookies
flour = cupsOfFlour * numOfCookies

# Display the number of cups for each ingredient needed
print(f'You will need {sugar:.1f} cups of sugar, {butter:.1f} cups of butter and {flour:.1f}'
      f' cups of flour to make {numOfCookies} cookies.')
