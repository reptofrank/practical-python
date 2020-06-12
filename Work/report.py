# report.py
#
# Exercise 2.4
import sys
import csv

def read_portfolio(filename):
	""" """
	portfolio = []
	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			holding = (row[0], int(row[1]), float(row[2]))
			portfolio.append(holding)


	return portfolio

if __name__ == '__main__':
	if len(sys.argv) == 2:
		print(read_portfolio(sys.argv[1]))