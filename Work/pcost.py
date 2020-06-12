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
		count = 1
		for row in rows:
			try:
				total += int(row[1]) * float(row[2])
			except ValueError:
				print(f'incomplete data on line {count}')
			count += 1
		return total

if len(sys.argv) == 2:
	file = sys.argv[1]
else:
	file = 'Data/portfolio.csv'
cost = portfolio_cost(file)
print('Total cost:', cost)