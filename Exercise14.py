# Prompt the user to enter information about money deposited
principalAmount = float(input('Enter the principal amount deposited: '))
annualIntRate = float(input('Enter annual interest rate: '))
compoundedRate = int(input('Enter the number of times per year that interest is compounded: '))
numOfYears = int(input('Enter the number of years the account will be left earning interest: '))

# Calculate compounding interest using formula
amount = principalAmount * (1+(annualIntRate/100)/compoundedRate)**(compoundedRate*numOfYears)

# Display the amount of money in the account after specified number of years
print(f'Amount of money in account after {numOfYears} years will be ${amount:,.2f}')
