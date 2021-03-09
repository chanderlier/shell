import csv

<<<<<<< HEAD
=======

>>>>>>> 6b1021d9d3d598f4bee7db58e54bca1456c0983b
def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
<<<<<<< HEAD
                 'name'   : record['name'],
                 'shares' : int(record['shares']),
                 'price'   : float(record['price'])
=======
                 'name': record['name'],
                 'shares': int(record['shares']),
                 'price': float(record['price'])
>>>>>>> 6b1021d9d3d598f4bee7db58e54bca1456c0983b
            }
            portfolio.append(stock)

    return portfolio

<<<<<<< HEAD
=======

>>>>>>> 6b1021d9d3d598f4bee7db58e54bca1456c0983b
def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

<<<<<<< HEAD
=======

>>>>>>> 6b1021d9d3d598f4bee7db58e54bca1456c0983b
def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
<<<<<<< HEAD
        change        = current_price - stock['price']
        summary       = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows
        
# Read data files and create the report data        

portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')

# Generate the report data

report    = make_report_data(portfolio, prices)

# Output the report
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)

=======
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows
# Read data files and create the report data        


portfolio = read_portfolio('python\practical-python-zh\Work\Data\portfolio.csv')
prices = read_prices('python\practical-python-zh\Work\Data\prices.csv')

# Generate the report data

report = make_report_data(portfolio, prices)


# Output the report
def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)


print_report(report)
>>>>>>> 6b1021d9d3d598f4bee7db58e54bca1456c0983b
