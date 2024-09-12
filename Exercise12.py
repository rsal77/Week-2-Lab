# Variables of stock purchase
numOfShares = 2000
pricePerSharePur = 40
pricePerShareSale = 42.75

# Calculate the amount paid for the stock
amtPaidStock = numOfShares * pricePerSharePur

# Calculate the amount received at sale
amtSoldStock = numOfShares * pricePerShareSale


# Calculate the interest paid on stock purchase
intPaidPur = (numOfShares * pricePerSharePur) * 0.03

# Calculate the interest paid on stock sale
intPaidSale = (numOfShares * pricePerShareSale) * 0.03

# Calculate the amount leftover after stock sold and interest paid
profit = amtSoldStock - amtPaidStock - intPaidPur - intPaidSale

# Display information about Joe's stock purchase and sale
print(f'Amount paid for stock ${amtPaidStock:,.2f}')
print(f'Amount of interest paid at purchase ${intPaidPur:,.2f}')
print(f'Amount received for stock sold ${amtSoldStock:,.2f}')
print(f'Amount of interest paid at sale ${intPaidSale:,.2f}')
print(f'Amount of money leftover ${profit:,.2f}')
