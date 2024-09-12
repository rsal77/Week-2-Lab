# Prompt the user for projected amount of total sales
totalSales = float(input('Enter the projected amount of total sales: '))

# Calculate the profit based on 23 percent of the total sales
profit = totalSales * 0.23

# Display the profit amount
print(f'Annual profit is ${profit:,.2f}')
