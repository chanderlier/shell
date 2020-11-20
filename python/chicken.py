#!/usr/bin/python3
a = 5
b = 3
c = 1 / 3
money = 100
for  i in range(0,20):
    for j in range(34):
        for k in range(0,30):
            if a * i + b * j + c* k == 100 and i + j + k == 100:
                print('gongji %d,muji %d,xiaoji %d', i,j,k)
