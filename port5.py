# port.py version with function

import csv

def read_portfolio(filename, *, errors='warn'):
    '''
    Reads a CSV file with name, date, shares, price data into a list
    :param filename:
    :return:
    '''

    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("errors must be one of 'warn', 'silent', 'raise'")

    portfolio = [] # List of records
    total = 0.0

    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip the header row
        for rowno, row in enumerate(rows, start=1):
            try:
               row[2] = int(row[2])
               row[3] = float(row[3])
            except ValueError as err:
                if errors == 'warn':
                    print('Row:', rowno, 'Bad row:', row)
                    print('Row:', rowno, 'Reason:', err)
                elif errors == 'raise':
                    raise # Reraises the last exception
                else:
                    pass # Ignore
                continue  # Skips to the next row
            #record = tuple(row) #(row[0], row[1], row[2], row[3]) #...
            record = {
                'name': row[0],
                'date': row[1],
                'shares': row[2],
                'price': row[3]
            }
            portfolio.append(record)
            total += row[2] * row[3]
    return portfolio

#total  = portfolio_cost('Data/missing.csv', errors='warn')
portfolio = read_portfolio('Data/portfolio.csv', errors = 'silent')
#print(portfolio)
#total  = portfolio_cost('Data/bogus.csv', errors='silent')
#total  = portfolio_cost('Data/missing.csv')
#print("Total cost: ", total)

total = 0.0

#for holding in portfolio:
#    total += holding[2] * holding[3] # Shares * price

for holding in portfolio:
    total += holding['shares'] * holding['price'] # Shares * price

#for name, date, shares, price in portfolio:
#    total += shares * price

print('Total cost: ', total)