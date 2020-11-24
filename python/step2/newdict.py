price = {
    'AAPL': 191.88,
    'GOOG': 1345.22,
    'IBM': 123.44,
    'ORCL': 55.23,
    'ACN': 166.33,
    'FB': 154.66,
    'AMAZ': 546.55
}

price2 = {key: value for key, value in price.items() if value > 100}
print(price2)
