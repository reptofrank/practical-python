# pcost.py
#
# Exercise 1.27
with open('Data/portfolio.csv', 'rt') as f:
	headers = next(f)
	total = 0
	for line in f:
		parts = line.split(',')
		total += int(parts[1]) * float(parts[2])

	print(f'Total cost {total}')