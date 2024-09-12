# Prompt user for the price of each item
item1 = float(input('Enter the price of item number 1: '))
item2 = float(input('Enter the price of item number 2: '))
item3 = float(input('Enter the price of item number 3: '))
item4 = float(input('Enter the price of item number 4: '))
item5 = float(input('Enter the price of item number 5: '))

# Calculate the subtotal of all items
subtotal = item1 + item2 + item3 + item4 + item5

# Calculate the sales tax
salesTax = subtotal * 0.07

# Calculate the total
total = subtotal + salesTax

# Display the subtotal, amount of sales tax and the total
print(f'Subtotal ${subtotal:,.2f}')
print(f'Sales Tax ${salesTax:,.2f}')
print(f'Total ${total:,.2f}')

