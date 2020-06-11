# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000
count = 0;

while principal > 0:
	count += 1
	# if principal < payment:
	# 	extrapayment = principal
	pay = payment + extra_payment if count >= extra_payment_start_month and count < extra_payment_end_month else payment
	# print("principal - {}".format(principal))
	principal = round(principal * (1+rate/12), 2)
	if principal < pay:
		pay = principal
	principal = principal - pay
	total_paid = total_paid + pay
	print(f"{count} {total_paid} {principal}")
    

print(f'Total paid: {total_paid}, Duration: {count} months')

