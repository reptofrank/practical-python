# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
count = 0;

while principal > 0:
    extrapayment = payment + 1000 if count < 12 else payment
    principal = principal * (1+rate/12) - extrapayment
    total_paid = total_paid + extrapayment
    count += 1

print('Total paid', total_paid, 'Duration', count)