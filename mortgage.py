# mortgage.py
#
#
# Find out how long to pay offa mortgage

principal = 371000

payment  = 1990.39

rate = 0.0264

total_paid = 0

num_months = 0

# Extra payment info
extra_payment  = 1000
extra_payment_start_month = 1
extra_payment_end_month = 60
month  = 0

out = open('shedule.txt', 'w') # open a file for writing

print('{:>5s} {:>10s} {:>10s} {:>10s}'.format('Month', 'Interest', 'Principal', 'Remaining'), file=out)
while principal > 0:
    month += 1
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        total_payment = payment + extra_payment
    else:
        total_payment = payment
    interest = principal*rate/12
    principal = principal + interest - total_payment
    total_paid += total_payment
    num_months += 1
    print('{:>5d} {:>10.2f} {:>10.2f} {:>10.2f}'.format(month, interest, total_payment-interest, principal), file=out)

out.close()

print(f'Total paid: {total_paid} in {num_months} months')