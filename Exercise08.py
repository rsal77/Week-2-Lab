# Prompt the user to enter the amount charged for food
amountChargedFood = float(input('Enter the amount charged for food: '))

# Calculate the tip
tip = amountChargedFood * 0.18

# Calculate the sales tax
salesTax = amountChargedFood * 0.07

# Calculate the total
total = amountChargedFood + tip + salesTax

# Display the amount charged for food, tip, sales tax and total amount
print(f'Food ${amountChargedFood:,.2f}')
print(f'Tip ${tip:,.2f}')
print(f'Sales Tax ${salesTax:,.2f}')
print(f'Total ${total:,.2f}')
