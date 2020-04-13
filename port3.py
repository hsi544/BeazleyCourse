# port.py version with function

import csv

def portfolio_cost(filename):
    '''
    Computes total shares*price for a CSV file with name, date, shares, price data
    :param filename:
    :return:
    '''


    total = 0.0

    with open(filename, 'r') as f:
        # with open('Data/portfolio2.csv', 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip the header row
        #rowno = 0
        #for row in rows:
        for rowno, row in enumerate(rows, start=1):
            #rowno +=1
            # print(row)
            try:
               row[2] = int(row[2])
               row[3] = float(row[3])
            except ValueError as err:
                print('Row:', rowno, 'Bad row:', row)
                print('Row:', rowno, 'Reason:', err)
                continue  # Skips to the next row
            total += row[2] * row[3]

    return total

total  = portfolio_cost('Data/missing.csv')
print("Total cost: ", total)