# mortgage.py
#
# Exercise 1.7

#Parameters
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

#Extra
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
	month += 1

	if month >= extra_payment_start_month and month <= extra_payment_end_month:
		principal = principal * (1+rate/12) - payment - extra_payment
		total_paid += payment + extra_payment
	else:
		principal = principal * (1+rate/12) - payment
		total_paid += payment

	print(f'{month:5d} {round(total_paid,2):10.2f} {principal:10.2f}')

#Correct for overpayment
total_paid += abs(principal)
principal = 0

	

print(f'Months taken: {month:5d}')
print(f'Total paid: {round(total_paid,2):5.2f}')


