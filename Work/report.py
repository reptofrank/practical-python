# report.py
#
# Exercise 2.4
import sys
import csv

def read_portfolio(filename):
	"""read portfolio information from csv file and return in an array of tuples"""
	portfolio = []
	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
			portfolio.append(holding)


	return portfolio


def read_prices(filename):
	""" """
	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		prices = {}
		for row in rows:
			if row:
				prices[row[0]] = float(row[1])

		return prices


def make_report():
	portfolio = read_portfolio('Data/portfolio.csv')
	new_prices = read_prices('Data/prices.csv')

	report = []

	for stock in portfolio:
		new_price = new_prices[stock['name']]
		diff = new_price - stock['price']
		report.append((stock['name'], stock['shares'], new_price, float(f'{diff:0.2f}')))

	return report

if __name__ == '__main__':
	if len(sys.argv) == 2:
		print(read_portfolio(sys.argv[1]))
