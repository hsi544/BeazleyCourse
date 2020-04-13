# port6.py version with function

import reader

def read_portfolio(filename, *, errors='warn'):
    '''
    Reads a CSV file with name, date, shares, price data into a list
    :param filename:
    :return:
    '''
    return reader.read_csv(filename, [str, str, int, float], errors=errors)

if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv', errors = 'silent')

    total = 0.0


    for holding in portfolio:
        total += holding['shares'] * holding['price'] # Shares * price


    print('Total cost: ', total)