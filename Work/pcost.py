# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):
	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)

		total = 0
		# count = 1
		for i, row in enumerate(rows, start=1):
			record = dict(zip(headers, row))
			try:
				total += int(record['shares']) * float(record['price'])
			except ValueError:
				print(f'incomplete data on line {i} - {row}')
		return total

if len(sys.argv) == 2:
	file = sys.argv[1]
else:
	file = 'Data/portfoliodate.csv'
cost = portfolio_cost(file)
print('Total cost:', cost)