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
	report = make_report()
	headers = ('Name', 'Shares', 'Price', 'Change')
	print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
	empty = ''
	print(f'{empty:->10s} {empty:->10s} {empty:->10s} {empty:->10s}')
	for name, shares, price, change in report:
		sym_price = f'${price}'
		print(f'{name:>10s} {shares:>10d} {sym_price:>10s} {change:>10.2f}')
