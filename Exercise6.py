# Prompt user for the amount of a purchase
amountOfPurchase = float(input('Enter the amount of purchase: '))

# Calculate the state sales tax
stateSalesTax = amountOfPurchase * 0.05

# Calculate the county sales tax
countySalesTax = amountOfPurchase * 0.025

# Calculate the total sales tax
totalSalesTax = stateSalesTax + countySalesTax

# Calculate the total of sale
total = amountOfPurchase + totalSalesTax

# Display the amount of purchase, state sales tax, county sales tax and total of purchase.
print(f'Purchase Amount ${amountOfPurchase:,.2f}')
print(f'State Sales Tax ${stateSalesTax:,.2f}')
print(f'County Sales Tax ${countySalesTax:,.2f}')
print(f'Total Sales Tax ${totalSalesTax:,.2f}')
print(f'Total ${total:,.2f}')