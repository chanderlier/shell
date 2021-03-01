#!/usr/bin/python3
res = []
f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')
sum = 0
for line in f:
    row = line.split(',')
    sum = sum + int(row[1]) * float(row[2])
f.close()
print('Total cost',sum)
