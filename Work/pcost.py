# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
	with open(filename, 'rt') as f:
		headers = next(f)
		total = 0
		for line in f:
			parts = line.split(',')
			total += int(parts[1]) * float(parts[2])
		return total

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)