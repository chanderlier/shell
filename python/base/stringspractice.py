import re
symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
# print(symbols.lower())

text = 'Today is  2/26/2021. Tomorrow is 2/27/2021.'
print(re.findall(r'\d+/\d+/\d+', text))
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

symlist = symbols.split(',')
print(symlist)


res = []
f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')
sum = 0
for line in f:
    cow = line.split(',')
    res.append(cow)
for i in range(len(res)):
    data = res[i]
    sum = sum + int(data[1]) * float(data[2])
f.close()
print('Total cost', sum)
