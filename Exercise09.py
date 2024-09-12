# This program will convert the temperature from Celsius to Fahrenheit

# Prompt the user to enter the temperature in Celsius
tempC = float(input('Enter the temperature in Celsius: '))

# Calculate the temperature to Fahrenheit using formula for conversion
tempF = (tempC * 9 / 5) +32

# Display the temerature in Fahrenheit
print(f'The temperature is {tempF:.1f} degrees Fahrenheit')
