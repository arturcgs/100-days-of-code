
print('Welcome to the tip calculator.')

total = float(input('What was the total bill? '))
n_people = float(input('How many people to split the bill? '))
tip = float(input('What percentage tip would you like to give? 10, 12 or 15? '))

print(f'Each person should pay: ${(total * ((tip / 100) + 1)) / n_people :.2f}')