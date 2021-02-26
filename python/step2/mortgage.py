principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
res = []

extra_payment = 1000.00
extra_payment_start_month = 1
extra_payment_end_month = 12

while principal > 0:
    month = month + 1
    principal = principal * (1 + rate/12) - payment
    res.append(principal)
    if principal > payment:
        total_paid = total_paid + payment
    else:
        total_paid = total_paid + res[-2] * (1 + rate/12)
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    print(month, round(total_paid, 2), round(principal, 2))
print('Total paid', round(total_paid, 2))
print('Months', month)
