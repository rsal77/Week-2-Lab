# Prompt user for the number of lions and tigers
lions = int(input('Enter the number of lions: '))
tigers = int(input('Enter the number of tigers: '))

# Variable for the total amount of animals
animals = lions + tigers

# Calculate the percentage of lions and tigers in the exibit
percentOfLions = lions / animals
percentOfTigers = tigers / animals

# Display the percentage of lions and percentage of tigers
print(f'The percentage of lions is {percentOfLions:.0%}')
print(f'The percentage of tigers is {percentOfTigers:.0%}')