# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
	with open(filename, 'rt') as f:
		headers = next(f)
		total = 0
		count = 1
		for line in f:
			try:
				parts = line.split(',')
				total += int(parts[1]) * float(parts[2])
			except ValueError:
				print(f'incomplete data on line {count}')
			count += 1
		return total

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)