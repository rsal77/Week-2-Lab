# Prompt the user miles driven
milesDriven = float(input('Enter the number of miles driven: '))

# Prompt the user for gallons of gas used
gallonsOfGas = float(input('Enter the number of gallons of gas used: '))

# Calculate the MPG using miles driven divided by gallons of gas used
mpg = milesDriven / gallonsOfGas

# Display MPG
print(f'The cars MPG is {mpg:.1f}')