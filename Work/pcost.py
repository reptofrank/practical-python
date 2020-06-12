# pcost.py
#
# Exercise 1.27
import csv

def portfolio_cost(filename):
	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		total = 0
		count = 1
		for row in rows:
			try:
				total += int(row[1]) * float(row[2])
			except ValueError:
				print(f'incomplete data on line {count}')
			count += 1
		return total

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)